def f():
    print("yo")

class A:
    
    def __init__(self):
        self.param = 10
        print("yep")

if __name__ == "__main__":
    # un objet python qui implémente sa fonction magique __call__
    # peut utilier l'opérateur (),  qui appelle __call__
    # un tel objet est appelé callable
    f.__call__()
    f()
    # avec les classes, on voit que __call__ appelle __init__
    A.__call__()
    A()
    