def normal_function():
    return "value"

# fonction génératrice
def generator_function():
    yield "first value"
    yield "second value"
    yield "third value"
    yield

if __name__ == "__main__":
    # retourne la valeur en face du premier return rencontré
    val = normal_function()
    print(val)
    # retourne l'objet générateur, à exécuter via next() ou for
    gen = generator_function()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    # un yield vide renvoie None
    print(next(gen))
    # StopIteration
    # print(next(gen))
    
    # via for
    for value in generator_function():
        print(value)
    