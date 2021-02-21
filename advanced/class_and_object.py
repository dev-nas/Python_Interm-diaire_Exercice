class A:
    # attribut de classe
    param = 100
    
    def __init__(self, *args):
        # attribut d'instance
        for arg in args:
            self.param = arg
    
    def some_method(obj):
        return obj.param
    
    @classmethod
    def some_class_method(cls):
        return cls.param
    
    @staticmethod
    def some_static_method(obj):
        print("some_extern_treatment")
        print(obj.param)
        

if __name__ == "__main__":
    # affiche l'attribut de classe
    print(f"attribut de classe: {A.param}")
    a = A()
    # affiche l'attribut d'instance
    # les attributs d'instance sont copiés d'après les attributs de classe
    print(f"attribut d'instance par défaut: {a.param}")
    a = A(10)
    print(f"attribut d'instance par instanciation: {a.param}")
    # les attributs de classes sont idépendants des attributs d'instance
    print(f"attribut de classe après instanciation: {A.param}")
    # méthode d'instance
    print(f"methode d'instance: {a.some_method()}")
    # méthode de classe : pas de paramètre obligatoire par défaut
    # on triche en injectant la classe
    # pas pratique
    print(f"methode de classe par défaut: {A.some_method(A)}")
    # on préférera une méthode de classe décorée par @classmethod
    # injectant la lasse en premier paramètre
    print(f"methode de classe décorée par classmethod: {A.some_class_method()}")
    # la méthode est utilisatble par les instances, mais le premier paramètre reste 
    # la classe "cls" et non l'instance "self"
    print(f"methode de classe appelée par l'objet: {a.some_class_method()}")
    # méthode statique au sens de python: accès sans les méthodes et attributs
    # traitements externes 
    A.some_static_method()
    a.some_static_method()
    