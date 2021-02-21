# fonction décoratrice
def decorator(f):
    def new_behaviour(*args, **kwargs):
        return f"résultat: {f(*args, **kwargs)}"
    # cas classique : on retourne la fonction implicite
    return new_behaviour

@decorator
# fonction décorée
def add(a, b) : 
    return a + b

# strictement équivalent à
# add = decorator(add) = new_behaviour
# Le décorateur est appliqué à la définition de la fonction décorée

if __name__ == "__main__":
    print(add(2, 2))