class CountInstances():
    nb_instances = 0

    def __init__(self) :
        CountInstances.nb_instances += 1 # opération sur l’attribut de classe
        
    @classmethod
    def count_instances(cls):
        return cls.nb_instances

if __name__ == "__main__":
    print(CountInstances.count_instances())
    for i in range(3):
        ci = CountInstances()
        print(CountInstances.count_instances())
    