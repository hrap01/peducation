#jak ta funkce volá sebe sama tak přibývá vrstev

#module os a pod ním je os.path - starší přístup a u novéého projektu se vyhnout, je postavený tak že tam jsou funkce isdir a tomu posíláš cestu
#pathlib funguje obráceně, ale tam je středobodem cesta a je to objekt na který voláš metody isfile, není to funkce kde bych dávala cestu, ale na tu cestu volám metody

import pathlib
import os.path
p = pathlib.Path(r'C:\Users\E12812')
p /= 'Documents'

def looking_for_files(path: pathlib.Path, excluded_files: list, included_files: list): #typové anotace
    try:
        dir_list = os.listdir(path)
        for item in dir_list:
            p = path / item
            if p.is_dir():
                looking_for_files(p, excluded_files, included_files)
            else:
                included_files.append(item)
    except PermissionError as pe:
        excluded_item = (str(path).rsplit('\\', 1))[1]
        excluded_files.append(excluded_item)
    #return excluded_files, included_files -  funkce nemusi nic vracet (radek 20), protoze listy se predavaji odkazem a navratova hodnota se nikde nepouziva

a = []
b = []
looking_for_files(p, a, b)


#Chci to ne vypsat, ale chceme to vrátit jako list, list všech souboru co se mi povedli vypsat a druhý kde se nepovedli
#musim používat ten samí list - ten list si musím poslat parametrem, vyřešit to parametrem, nechceme globální proměnnou