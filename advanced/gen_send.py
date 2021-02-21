def queue(*args):
    elems = list(args)
    while elems:
        # yield elems.pop(0)
        # l’exécution s’interrompt avant l’affection
        # yield contrairement à return peut être affecté
        # par défaut l'expression yield retourne None
        # la valeur en face de yield n'est récupérée que par next ou for
        new = yield elems.pop(0)
        print(f"reste dans elems: {elems}")
        print(f"retour de yield: {new}")
        if new is not None:
            elems.append(new)
    
if __name__ == "__main__":
    q = queue('a', 'b', 'c')
    for elem in q:
        print("--------for-iteration------------")
        print(f"valeur dans for: {elem}")
        if elem  == 'a':
            # send exécute une itération
            # et récupère le yield à la place du for
            # la valeur 'd' est affectée comme valeur de retour du yield courant
            print(f"valeur dans for: {q.send('d')}")