import os

class Cd :
    
    def __init__(self, path):
        self.path = path
        self.old_paths = []
        
    def __enter__(self):
        self.old_paths.append(os.getcwd())
        os.chdir(self.path)
        print(os.getcwd())

    def __exit__(self, *args):
        os.chdir(self.old_paths.pop())


if __name__ == "__main__":
    
    with Cd(".."):
        with Cd("./projet"):
            pass
    
    print(os.getcwd())