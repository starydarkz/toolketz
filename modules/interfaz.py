#DefaultTheme

from colorama import Fore, init
init()



def themes(): #Temas de toolketz

    from config.default_config import currenttheme
    ''' Temas de Toolketz '''
    theme1 ={
        "name":"Tema1",
        "color1":Fore.LIGHTCYAN_EX,
        "color2":Fore.LIGHTYELLOW_EX,
        "color3":Fore.WHITE,
        "special":Fore.RED,
        "word":Fore.LIGHTWHITE_EX
    }

    #Theme2
    theme2 ={
        "name":"Tema2",
        "color1":Fore.YELLOW,
        "color2":Fore.WHITE,
        "color3":Fore.LIGHTMAGENTA_EX,
        "special":Fore.LIGHTCYAN_EX,
        "word":Fore.LIGHTCYAN_EX
    }
    #Theme3
    theme3 ={
        "name":"Tema3",
        "color1":Fore.GREEN,
        "color2":Fore.YELLOW,
        "color3":Fore.WHITE,
        "special":Fore.LIGHTWHITE_EX,
        "word":Fore.LIGHTGREEN_EX
    }

    if currenttheme == 1:
        return theme1
    elif currenttheme == 2:
        return theme2
    elif currenttheme == 3:
        return theme3


def installed_apps(theme):
    from modules.basicfuncs import readcsv

    category = []
    text = ""
    installed_apps = readcsv("config/installed_apps.csv")
    selapp = []
    num = 0

    #Extraer Categoria
    for element in installed_apps:

        if element[0] not in category:
            category.append(element[0])
    
    for cat in category:
        app = ""
        for element in installed_apps:
            if element[0] == cat:
                num += 1
                selapp.append((num, element[2]))
                try:
                    app += str(num) + "| " + element[1] + "\n"
                except:
                    pass
        try:
            text += "\n" + theme["color3"] + "    " + cat + "\n" + theme["color2"] +app
        except:
            pass
        

    return text, selapp
      


def menu(theme=themes()): # Menu de toolketz

    
    tools, selapp = installed_apps(theme)

    mainmenu = (theme["color1"] + """
TTTTTTTTTTTTTTTTTTTTTT                              llllll  KKKKKKK                       KKKKKK
T::::::::::::::::::::T                       ____   l::::l  K:::::K                       K::::K
T::::::::::::::::::::T                       l::l   l::::l  K:::::K                       K::::K
T:::::TT::::::TT:::::T                       l::l   l::::l  K:::::K                       K::::K
TTTTTT  T::::T  TTTTTTooooooo    ooooooooo   l::l    K:::K  K:::::K    eeeeeeeeeeee   ttttt:::ttttttt  zzzzzzzzzzzzz
        T::::T     oo::::::::oo oo:::::::oo  l::l    K:::K K:::::K     ee::::::::::::eet:::::::::::::t  z::::::::::z
        T::::T    o::::::::::::oo::::::::::o l::l    K::::K:::::K     e::::::eeeee:::::et::::::::::::t  z::::::::::z
        T::::T    o:::ooooo:::oo:::ooooo:::o l::l    K:::::::::K     e::::::e     e:::::tttt::::tttttt  zzzzzz::::z
        T::::T    o::o     o::oo::o     o::o l::l    K:::::::::K     e:::::::eeeee::::::e t::::t             z:::z
        T::::T    o::o     o::oo::o     o::o l::l    K::::K:::::K    e:::::::::::::::::e  t::::t            z:::z
        T::::T    o::o     o::oo::o     o::o l::l    K::::K K::::K   e::::::eeeeeeeeeee   t::::t           z:::z
        T::::T    o::o     o::oo::o     o::o l::l    K::::K  K::::KKKe:::::::e            t::::t    ttttttz:::z
      TT::::::TT  o:::ooooo:::oo:::ooooo:::o l::::::lK::::K   K::::Ke::::::::e            t:::::tttt:::::tz::::zzzzz
      T::::::::T  o:::::::::::oo::::::::::o  l::::::lK::::K    K::::K e::::::::eeeeeeee    tt::::::::::::tz::::::::z
      TTTTTTTTTT   ooooooooooo  oooooooooo   llllllllKKKKKKK   KKKKKKK eeeeeeeeeeeeee       ttttttttttttzzzzzzzzzzzz
____________________________________________________________________________________________________________________
TTTTTTTTTTTTTTTTT|"""+theme["special"]+"Create By: Stary Dark"+theme["color1"] +"""|TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
    """+theme["color2"] +f"{tools} \n\n" +theme["color3"] +"--->" +theme["word"])

    inputuser = (input(mainmenu))
    
    from os import system
 
    
    if inputuser == "0":
        from input.config import install
        install()


    for numapp in selapp:
        if inputuser == str(numapp[0]):
            system(f"python modules/{numapp[1]}")
    




