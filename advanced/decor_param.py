# 1/ écrire la fonction à décorer
def param_print_decorator(before, after): # Décorateur paramétré
    def decorator(function): # Décorateur
        def new_function(*args, **kwargs): # Fonction qui remplacera la fonction décorée
            print(before.format(function.__name__, args, kwargs))
            ret = function(*args, **kwargs)
            print(after.format(ret))
            return ret
        return new_function
    return decorator

@param_print_decorator('call {} with args({}) and kwargs({})', 'ret={}')
def test_func(x):
    return x

@param_print_decorator('func {}: avant formatage: {}, options: {}', 'après formatage: {}')
def test_func2(msg):
    return msg.capitalize()

if __name__ == "__main__":
    print(test_func(4))
    print(test_func2("bonjour"))