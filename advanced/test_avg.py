import sys

def avg(l: list):
    return sum(l)/len(l)


if __name__ == "__main__":
    # test utilisant une assertion
    l = []
    rslt = 0
    # on utilise la liste sys.argv pout récupérer les arguments de la 
    # ligne de commande (python fichier.py arg1 arg2 arg3....)
    # argv[0] contient toujours la commande entière
    # les arguments commencent à 1
    # penser à convertir les arguments numériques
    if len(sys.argv) > 1:
        rslt = float(sys.argv.pop())
        for arg in sys.argv[1:]:
            l.append(int(arg))
    try:
        assert len(l), "list cannot be empty"
        assert avg(l) == rslt, "wrong result"
    except AssertionError as ae:
        print(ae)
    else:
        print("tests are OK!")    