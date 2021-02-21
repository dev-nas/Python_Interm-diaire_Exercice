from sys import getsizeof

# paramètres variables -> *args ou **kwargs
def gen_range(*params):
    # les trois paramètres possibles
    # selon le nombre de paramètres
    start = params[0] if len(params) > 1 else 0
    end = params[1] if len(params) > 1 else params[0]
    incr = params[2] if len(params) > 2 else 1

    while start < end:
        yield start
        start += incr
    
if __name__ == "__main__":
    g_range1 = gen_range(5)
    print("g_range(5)")
    for i in g_range1:
        print(i)
    g_range2 = gen_range(2, 5)
    print("g_range(2, 5)")
    for i in g_range2:
        print(i)
    g_range3 = gen_range(2, 12, 3)
    print("g_range(2, 12, 3)")
    for i in g_range3:
        print(i)
    
    g10e5 = gen_range(100000)
    print(f"size of gen_range(10e5) : {getsizeof(g10e5)}")
    print(f"size of list(10e5) : {getsizeof(list(g10e5))}")
    # range est un générateur
    print(f"size of range(10e5) : {getsizeof(range(100000))}")
    
    