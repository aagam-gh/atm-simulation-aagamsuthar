import hashlib
from datetime import datetime

pin_hash = hashlib.sha256("1234".encode()).hexdigest()
balance = 5000
history = []


def save(kind, amount):
    t = datetime.now().strftime("%d-%m-%Y %H:%M")
    line = t + " - " + kind + " - Rs." + str(amount) + " - balance Rs." + str(balance)
    history.append(line)
    f = open("transactions.txt", "a")
    f.write(line + "\n")
    f.close()


def login():
    tries = 0
    while tries < 3:
        pin = input("Enter PIN: ")
        if hashlib.sha256(pin.encode()).hexdigest() == pin_hash:
            print("Login successful")
            return True
        tries += 1
        print("Wrong PIN,", 3 - tries, "tries left")
    print("Card blocked")
    return False


def deposit():
    global balance
    amt = int(input("Amount to deposit: "))
    if amt > 0:
        balance += amt
        save("deposit", amt)
        print("Done. Balance:", balance)
    else:
        print("Invalid amount")


def withdraw():
    global balance
    amt = int(input("Amount to withdraw: "))
    if amt <= 0:
        print("Invalid amount")
    elif amt > balance:
        print("Not enough balance")
    else:
        balance -= amt
        save("withdraw", amt)
        print("Done. Balance:", balance)


def statement():
    if len(history) == 0:
        print("No transactions yet")
    for h in history[-5:]:
        print(h)


print("---- ATM ----")
if login():
    while True:
        print("\n1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Exit")
        ch = input("Choose: ")
        if ch == "1":
            print("Balance:", balance)
        elif ch == "2":
            deposit()
        elif ch == "3":
            withdraw()
        elif ch == "4":
            statement()
        elif ch == "5":
            print("Bye")
            break
        else:
            print("Wrong choice")
