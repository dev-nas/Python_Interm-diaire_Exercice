from time import time, sleep

class Timer():
    
    def __enter__(self):
        self.start = time()
    
    def __exit__(self, *args):
        print(time() - self.start)


if __name__ == "__main__":
    
    with Timer():
        sleep(3)
    
    print("out of context!")
    