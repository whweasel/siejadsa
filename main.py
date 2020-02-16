for _ in [0]: # IMPORT STATEMENTS
    """ IMPORT STATEMENTS """
    from blessed import Terminal; # "mother" library class, used for debug purposes
    from scrtools import stream; # base class for most common methods
    from scrtools import color; # color class, for support of colors
    from scrtools import colors; # colors class, containing some predefined colors
    from scrtools import symbols; # symbols class, containing some symbols
    import textrpglib as rpg
    import os
    import sys
    os.chdir(sys.path[0])
    pass; # IMPORT STATEMENTS
for _ in [1]: # SCRTOOLS SETTINGS
    """ SCRTOOLS SETTINGS """
    stream.menu_select_keys = ["KEY_Z", "KEY_ENTER"]; # confirmation keys for menus
    stream.menu_cursor_color = colors.red; # color that the cursor will be shown in, for menus
    stream.menu_highlight_color = colors.yellow; # color that selected text will be shown in, for menus
    stream.menu_cursor = symbols.triangle; # string representing what the cursor shall look like.
    stream.echo_escape_keys = ["KEY_X"]; # keys that will bypass the "typewriter" effect for the echo() method, and print the body all at once
    stream.sleep_escape_keys = ["KEY_Z", "KEY_ENTER"]; # sleep escape keys
    stream.default_end = ''; #default value for the end variable. DON'T CHANGE THIS UNLESS YOU KNOW WHAT YOU'RE DOING!
    
    pass; # SCRTOOLS SETTINGS
for _ in [2]: # PRE-RUN OPERATIONS
    """ PRE-RUN OPERATIONS """
    t = Terminal();
    print("Garbage collection in progress\nDo not close this window...")
    stream.collect()
    stream.clear()
    print(t.red("Do NOT resize this window when the program is running, it will break the game!\nSuggestion: Use Fullscreen!"))
    print("Press [Z]/[ENTER] to continue")
    stream.pause()
    stream.clear()
    pass; # PRE-RUN OPERATIONS
def menuClosure(header, content, *, delay_ms = 34, tfactor = 6, factor = 4):
    def inner_function():
        return stream.menu(header, content, delay_ms = delay_ms, tfactor = tfactor, factor = factor)
    return inner_function

game_title = "One doesn't mean all, right?\n"

for _ in ["title"]:
    try:
        rpg.data.load("playerdata.dat")
    except EOFError:
        playerdata = rpg.data()
        titleList = ["Start", t.gray30("[DISABLED] Continue"), "Help/Credits", "Exit\n\n" + "   " + " "* int(stream.width()/4) + t.white("CONTROLS:\n") + " "* int(stream.width()/5) + t.gray30("[ENTER] and [Z] - Confirm Selection\n") + " "* int(stream.width()/4.5) + t.gray30("Arrow Keys - Move Cursor")]
    else:
        playerdata = rpg.data.load("playerdata.dat")
        titleList = ["Start", "Continue", "Help/Credits", "Exit\n\n" + "   " + " "* int(stream.width()/4) + t.white("CONTROLS:\n") + " "* int(stream.width()/6) + t.gray30("[ENTER] and [Z] - Confirm Selection\n") + " "* int(stream.width()/4.5) + t.gray30("Arrow Keys - Move Cursor")]
    finally:
        title_screen = menuClosure(game_title, titleList, delay_ms = 24, tfactor = 5)

for _ in [2]:
    def game_intro():
        delay = [60, 1, 80, 800]
        stream.collect()
        stream.clear()
        _ = rpg.frontend.block([("Long ago, two nations dominated the Earth:\n"), ("The ", colors.red.w("SOVIET UNION"), ", and the ", colors.green.w("UNITED STATES OF AMERICA"))], delay[2], 0, check=None, cont=False)
        _ = None
        stream.sleep(1700, allow_escape = True)
        stream.clear()
        _ = rpg.frontend.block([("The ", colors.green.w("U.S.A"), " believed in freedom and justice for all.\n"), "They were opposed to war of any kind."], delay[0], delay[1], end='', check=_, cont=False)
        _ = None
        stream.sleep(1400, allow_escape = True)
        stream.clear()
        _ = rpg.frontend.block([("The ", colors.red.w("U.S.S.R"), ", however, hated progressivism.\n"), ("The State controlled all aspects of life, and all her\n"), ("people suffered through famine, oppression, and poverty.")], delay[0], delay[1], end='', check=None, cont=False)
        stream.sleep(1400, allow_escape = True)
        _ = None
        stream.clear()
        _ = rpg.frontend.block(["One day, war broke out between the two powers.\n", "Nobody survived the war. All life was destroyed."], delay[0], delay[1], end='', check=None, cont=False)
        _ = None
        stream.sleep(1000, allow_escape = True)
        stream.clear()
        _ = rpg.frontend.block([colors.red.w("But nobody remembered that."),("\n"), colors.red.w("Not even you.")], delay[0], 1500, end='', check=None, cont=False, factor=4)
        stream.sleep(2000, allow_escape = True)
        _ = None
        stream.clear()
        _ = rpg.frontend.block([colors.red.w("Instead, the U.S.S.R collapsed in 199X, becoming the Russian\n"), colors.red.w("Federation.\n")], delay[0], delay[1], end='', check=None, cont=False)
        _ = rpg.frontend.block([colors.red.w("Russia was weak. The U.S.A was weak.\n")], delay[0], delay[1], end='', check=_, cont=False, begin='')
        stream.pause()
        
    def game_cottonwood_1():

        stream.sleep(32768, allow_escape = True)

def help_credits():
    stream.clear()
    _ = rpg.frontend.block(["Copyright " + symbols.copyright + " 2020 DH93\n"], 40, 40, end='', check=None, cont=False)
    _ = rpg.frontend.block(["For help, see the title screen.\n\n"], 40, 40, end='', check=_, cont=False)
    _ = rpg.frontend.block([colors.gray.w("Press [Z]/[ENTER] to continue")], 40, 40, end='', check=_, cont=False)
    stream.pause()
    return title_screen


global funcls
funcls = [
    game_intro,
    game_cottonwood_1
]
for _ in [3]:
    def start_game():
        global funcls
        returnVal = title_screen();
        if returnVal == 4:
            stream.clear()
            try:
                os._exit(1)
            except:
                sys.exit()
        if returnVal == 1:
            lolindex = 0
        if returnVal == 2:
            try:
                lolindex = funcls.index(lastSave)
            except NameError:
                lolindex = 0
        if returnVal == 3:
            return help_credits
        for i in range(len(funcls[lolindex:])):
            funcls[i]()
        return title_screen





if __name__ == "__main__":
    """ ON-EXECUTE CODE """
    returned_value = start_game()
    i = 1
    while True:
        i += 1
        print(i)
        returned_value = returned_value()
    
    
    pass; # ON-EXEC CODE