def login(counter=3):
    username = input("username : ")
    password = input("password : ")
    if username != "admin" or password != "password":
        print("wrong user data")
        counter -= 1
        print(f"you still have {counter} tries left ")
        if counter == 0:
            print(
                "you have attemped all your tries, are you trying to hack this account ?"
            )
            return
        login(counter)
    else:
        print("welcome admin")


login()
