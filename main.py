
"""
Module de lecture de fichier texte ligne par ligne.
Ce module permet de lire un fichier texte et de retourner son contenu sous forme de liste de lignes.
"""

FILENAME = "listes.csv"

def read_data(filename):
    list_lines = []
    with open(filename, mode='r', encoding='utf8') as f:
        for elt in f:  
            elt = elt.strip()
            list_lines.append(elt)
            print(elt)
    return list_lines
    return list_lines

data = read_data(FILENAME)
print(data)

