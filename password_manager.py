from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", "rb")

    key = file.read()
    file.close()

    return key


print(b"hello")
key = load_key()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()

    with open("key.key","wb") as key_file:
        key_file.write(key)
'''


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:",user, ", Password:",fer.decrypt(password.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name+"|"+str(fer.encrypt(pwd.encode()).decode())+"\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

