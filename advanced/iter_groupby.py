from itertools import groupby

def get_occurences(txt):
    # trier le texte par ordre alpha bétique fait apparaitre les 
    # suites d'occurences de mots
    # la longueur du groupe associé à chaque mot donne l'occurence
    # occ = {}
    # for elem, group in groupby(sorted(txt.split())):
    #     occ[elem] = len(list(group))
    # return occ
    # bonus : dictionnaire en intension
    return {elem: len(list(group)) for elem, group in groupby(sorted(txt.split()))}

if __name__ == "__main__":
    print(get_occurences("appeler un chat un chat"))