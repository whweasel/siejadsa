import time
from blessed import Terminal
t = Terminal()
import os
import re

def sleep(times):
    with t.cbreak():
        t.inkey(timeout=times)

def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

def clear():
    print(t.clear, end='', flush=True)
    pass #no

def ms(milliseconds):
    """convert milliseconds to seconds"""
    return milliseconds/1000

class painted:
    def __init__(self, text, color_object):
        self.namedcolor = color_object.namedcolor
        self.color = color_object.color
        self.text = text
    def __str__(self):
        try:
            return self.color(escape_ansi(self.text))
        except TypeError:
            return self.color(self.text.text)

class color:
    def __init__(self, namedcolor):
        self.namedcolor = namedcolor
        self.color = getattr(t, namedcolor)
    def __call__(self, text):
        return painted(text, self)

def indent(text):
    if type(text) == painted:
        text.text = "      " + text.text
    else:
        text = "      " + text
    return text

def echo(text, delay=ms(37), *, end='\n', color=None):
    if color != None:
        print(getattr(t, color), end='', flush=True)
    if type(text) == painted:
        print(text.color, end='')
        for item in text.text:
            print(item, end='', flush=True)
        print(t.normal + end, end='', )
    elif type(text) == str:
        for char in text:
            print(char, flush=True, end='')
            time.sleep(delay)
        print(t.normal + end, flush=True, end='')

def wait():
    with t.cbreak():
        key = t.inkey(timeout=1/1000)
        key = t.inkey(timeout=1/1000)
        key = t.inkey(timeout=1/1000)
        key = t.inkey()
def catch_prekey():
    with t.cbreak():
        key = t.inkey(timeout=1/1000)
        key = t.inkey(timeout=1/1000)
        key = t.inkey(timeout=1/1000)
    
    
    while True:
            with t.cbreak():
                key = t.inkey()
                if key == "z" or key.name == "KEY_ENTER":
                    return

class Menu:
    selected_choice_color = color("gold1")
    @classmethod
    def menu(cls, title, contents):
        with t.cbreak():
            e = t.inkey(timeout=10/1000)
        os.system("cls")
        if type(contents) != dict:
            raise TypeError("Menu contents must be a dict.")
        with t.cbreak(): #event loop
            cursorPosition = 1
            echo(title, delay=ms(26))
            loc = t.get_location()[0]
            while True:
                print(t.move_y(loc), end='', flush=True)
                currentIter = 0
                for key in contents:
                    currentIter += 1
                    if currentIter == cursorPosition:
                        print("  " + str(cls.selected_choice_color(contents[key])), flush=True)
                        selected_key = key
                    elif currentIter != cursorPosition:
                        print("  " + str(contents[key]), flush=True)
                try:
                    del key
                except:
                    pass
                key = t.inkey()
                if key.name == "KEY_UP":
                    if cursorPosition == 1:
                        cursorPosition = len(contents)
                    elif cursorPosition != 1:
                        cursorPosition -= 1
                elif key.name == "KEY_DOWN":
                     if cursorPosition == len(contents):
                         cursorPosition = 1
                     elif cursorPosition != len(contents):
                         cursorPosition += 1
                elif key.name == "KEY_ENTER" or key == "z".lower():
                    return selected_key
