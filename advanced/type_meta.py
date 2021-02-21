class A:
    pass

# la classe B ...
class B(A):
    param = 5
    
    def func(self, x):
        return x + 1

# ...est équivalente à
B = type('A', (), {"param": 5, "func": lambda self, x: x + 1})


if __name__ == "__main__":
    b = B()
    print(b.param)
    print(b.gunc(3))