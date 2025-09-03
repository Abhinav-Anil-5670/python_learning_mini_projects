master_pwd = input("Enter Master Password: ")

def view():
    with open("passwords.txt",'r') as f: #r->read
         for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print(f"The Username is {user} and password is {passw}")
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt",'a') as f:#a->append
         f.write(name + "|" + pwd + "\n")



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