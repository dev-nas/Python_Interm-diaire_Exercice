import random

# fonction
def caesarize():
    chaine = "coucou"
    chaine = list(chaine)
    
    # même chose avec la fonction enumerate
    # permet d'itérer à la fois sur l'indice et l'élément
    for i, char in enumerate(chaine):
        if char == "c":
            chaine[i] = "f"
        elif char == "o":
            chaine[i] = "r"
        else:
            chaine[i] = "x"
    chaine = "".join(chaine)
    return chaine

# fonction paramétrée
# on peut indiquer les types attendus
# on procède au refactoring
def caesarize2(msg: str, shift=3):
    msg = list(msg)
    for i, char in enumerate(msg):
        # nouveau caractère correspond au caractère d'ordinal : ord("char") + shift
        # ajout d'un décalage au delà de z qui reboucle sur a
        msg[i] = chr(97 + ((ord(char) + shift - 97) % 26))
    return "".join(msg)

# génère une correspodance sur les lettres de l'alĥabet avec un déclalage
# spécifique pour chaque lettre
def get_key():
    # variables à mettre en correspondace
    letters, key = "abcdefghijklmnopqrstuvwxyz", []
    for char in letters:
        # génération d'un décalage par lettre via random
        # on boucle tant que l'on a pas trouvé un nouveau caractère
        while True:
            shift = random.randint(0, 25)
            # calcul du nouveau caractère
            new_char = chr(97 + ((ord(char) + shift - 97) % 26))
            # contôler que la valeur transorfmée n'est pas déjà attribuée
            if new_char not in key:
                key.append(new_char)
                # correspondance trouvée: on casse la boucle
                break
    return "".join(key)

# fonctionnement avec une clé de chiffrement
def caesarize3(msg: str, key: str):
    # conversion en liste
    msg = list(msg)
    for i, char in enumerate(msg):
        # le caractère de remplacement correspond à l'indice dans la clé de son ordinal
        msg[i] = key[(ord(char) - 97)]
    return "".join(msg)

# décryptage
def uncaesarize3(secret, key):
    secret = list(secret)
    for i, char in enumerate(secret):
        # l'index du caractère chiffré dans la lé donne l'ordinal du caractère en clair
        secret[i] = chr(97 + key.index(char))
    return "".join(secret)

# portage de la POO
class Caesar:
    # attribut "privé"
    _key = None
    
    # initialiseur
    def __init__(self, key):
        self._key = key
    
    # méthodes publiques
    def encrypt(self, msg: str):
        msg = list(msg)
        for i, char in enumerate(msg):
            msg[i] = self._key[(ord(char) - 97)]
        return "".join(msg)
    
    def decrypt(self, secret: str):
        secret = list(secret)
        for i, char in enumerate(secret):
            secret[i] = chr(97 + self._key.index(char))
        return "".join(secret)
    

# exécuter le module comme programme principal
if __name__ == "__main__":
    key = get_key()
    caesar = Caesar(key)
    secret = caesar.encrypt("maisouestdoncornicar")
    # f-strings : évolution de "..{}.".format(var)
    print(f"message chiffré: {secret}")
    print(f"message décrypté: {caesar.decrypt(secret)}")