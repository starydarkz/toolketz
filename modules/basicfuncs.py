






def clearwindow():
    ''' Esta funcion limpia la ventana'''
    from os import name, system
    if name == 'nt':
        system("cls")
    else:
        system("clear")




def readcsv(csvfile):
    """Lee un archivo csv y retorna una lista"""
    
    import csv
    with open(csvfile, 'r', encoding="utf8") as csvfile:
        content_csv = csv.reader(csvfile)
        result = []
        
        for fila in content_csv:
            result.append(fila)
        if len(result) == 1:
            lista = []
            for element in range(0,len(result[0])):
                lista.append(0)
            result.append(lista)         
    return result
