# fonction décoratrice
def decorator(f):
    print(f.__name__)
    # cas simple : la fonction retournée est la fonction décorée
    return f

@decorator
# fonction décorée
def add(a, b) : 
    return a + b

# strictement équivalent à
# add = decorator(add)
# Le décorateur est appliqué à la définition de la fonction décorée

if __name__ == "__main__":
    print("début du main")
    