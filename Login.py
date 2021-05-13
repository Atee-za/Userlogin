import sqlite3
conn = sqlite3.connect('users.db')


def menu():
    print("[ LOGIN SYSTEM ]")
    print("[0] EXIT")
    print("[1] LOGIN")
    print("[2] SIGN UP")
    print()
    x = int(input("  >>  "))
    return x


def login():
    print("[ LOGIN ]")
    username = input("ENTER USERNAME >>  ")
    password = input("ENTER PASSWORD >>  ")
    cursor = conn.execute("SELECT username, password from Staff where username == '" + username + "' and password == '" + password +"'")
    for row in cursor:
        print("Login Successful!")
        print()
        return
    print("Login Unseccessful, try again..")
    print()


def signup():
    print("[ SIGN UP ]")
    username = input("ENTER USERNAME >>  ")
    cursor = conn.execute("SELECT username from Staff where username == '" + username + "'")
    for row in cursor:
        print("Username Taken, try again..")
        print()
        return
    password = input("ENTER PASSWORD >>  ")
    insert(username, password)


def insert(username, password):
    conn.execute("INSERT INTO Staff (USERNAME,PASSWORD) VALUES ('"+username+"', '"+password+"');")
    conn.commit()
    print("Successfully SIGNED UP")
    print()


loop = menu()
while loop != 0:
    if loop == 1:
        login()
    elif loop == 2:
        signup()
    else:
        print("Ivalid Option, try again..")
    loop = menu()
print("Exited")
conn.close()

