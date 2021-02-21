# 1/ écrire la fonction à décorer
# 2/ créer le décorateur avec un paramètre fonction
# 3/ créer la fonction implicite qui sera retournée 
# par le décorateur
# 4/ manipuler la fonction décorée dans la fonction implicite
# 5/ la fonction retournée doit posséder la signature de 
# la fonction décorée
# 6/ décorer la fonction avec "@"
def bold(func):
    def wrap(content):
        return f"<strong>{func(content)}</strong>"
    return wrap

def italic(func):
    def wrap(content):
        return f"<em>{func(content)}</em>"
    return wrap

# on peut enchaîner les décorateurs
@bold
@italic
def get_title(content):
    return content.upper()

if __name__ == "__main__":
    print(get_title("test"))    