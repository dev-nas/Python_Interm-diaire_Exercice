def infinite_atm(bill=20):
    while True:
        yield bill

if __name__ == "__main__":
    balance = 500
    # générateur infini:  doit être géré dans la boucle
    for b in infinite_atm():
        if balance <= 0:
            print(f"{balance} €: BROKE!")
            break
        balance -= b
        print(balance)
        
    