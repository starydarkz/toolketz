"""#Archivo de configuracion por defecto"""

# Temas
currenttheme = 1


#Apps

def exect_apps():
    from modules.basicfuncs import readcsv

    file = readcsv("config/Installed_apps.csv")
    
