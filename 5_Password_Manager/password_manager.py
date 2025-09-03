from cryptography.fernet import Fernet



# def write_Key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

def read_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key





key = read_key() 
fer = Fernet(key)

def view():
    with open("passwords.txt",'r') as f: #r->read
         for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("The Username is", user, "and password is " ,  fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt",'a') as f:#a->append
         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") #encode -> to convert it into bytes



while True:
    mode = input("Would you like to view passords or add a new one? (view/add) or press q to exit: ").lower()
    if mode =="q":
        break
    if mode =="view":
        view()
    elif mode == "add":
       add()
    
    else:
        print("Invalid Mode")