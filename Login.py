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
    if len(username) == 0:
        print("Username required! \n")
        return
    password = input("ENTER PASSWORD >>  ")
    if len(password) == 0:
        print("Password required! \n")
        return
    cursor = conn.execute("SELECT username, password from Staff where username == '" + username + "' and password == '" + password +"'")
    for row in cursor:
        print("Login Successful! \n")
        return
    print("Login Unseccessful, try again.. \n")


def signup():
    print("[ SIGN UP ]")
    username = input("ENTER USERNAME >>  ")
    if len(username) == 0:
        print("Username required! \n")
        return
    cursor = conn.execute("SELECT username from Staff where username == '" + username + "'")
    for row in cursor:
        print("Username Taken, try again.. \n")
        return
    password = input("ENTER PASSWORD >>  ")
    if len(password) == 0:
        print("Password required! \n")
        return
    insert(username, password)


def insert(username, password):
    conn.execute("INSERT INTO Staff (USERNAME,PASSWORD) VALUES ('"+username+"', '"+password+"');")
    conn.commit()
    print("Successfully SIGNED UP \n")


loop = menu()
while loop != 0:
    if loop == 1:
        login()
    elif loop == 2:
        signup()
    else:
        print("Invalid Option, try again..")
    loop = menu()
print("Exited")
conn.close()

