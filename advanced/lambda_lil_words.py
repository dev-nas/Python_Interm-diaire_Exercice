from time import time

def strip_lil_words(txt, nb):
    return " ".join([word for word in txt.split() if len(word) > nb])

def filter_lil_words(txt, nb):
    # on traduit la condition "if len(word) > nb" dans une lambda pour filtrer
    # les mots du texte
    return " ".join(filter(lambda word: len(word) > nb, txt.split()))

if __name__ == "__main__":
    # le temps d'exécution d'une commande est la diiférence de timestamps
    # précédents et suivants une instruction
    start = time()
    print(strip_lil_words("test test test ee ee ee lzekjf lezkrh lkazer", 3))
    print(time() - start)
    
    start = time()
    print(filter_lil_words("test test test ee ee ee lzekjf lezkrh lkazer", 3))
    print(time() - start)
    