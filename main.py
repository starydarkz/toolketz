#Version 1.0

from modules.basicfuncs import clearwindow
#menu




def mainmenu():
    from modules.interfaz import menu
    from os import system
    clearwindow()
    menu()
    clearwindow()

def main():
    while True:
        mainmenu()

main()
