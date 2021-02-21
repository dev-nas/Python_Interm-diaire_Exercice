def test_close():
    for i in range(5):
        try:
            yield i
        except GeneratorExit:
            break

if __name__ == "__main__":
    
    tc = test_close()
    for i in tc:
        print(i)
        if i == 3:
            tc.close()