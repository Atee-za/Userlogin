USER LOGIN SYSTEM

    This Application was created using JetBrains PyCharm. The Application 
    allows a user to Login or SignUp using System Terminal/Console. The 
    data is saved in a database 'users.db' under the 'Staff' table.

Prerequisites:

    Python IDE or Terminal are required to run this application. Clone the
    project into your local repository then navigate to the root of application
    in your terminal.

How it works:
    
    A new user Sign Up with a unique username. After entering the username the system check
    from the database if the username is unique or not.
    If it does exist the system will display a message that the username already exist.
    The system stops and the user needs to signup using a different unique username.
    
    If the username is unique the system will prompt a password entry where the user enters the
    password. The password does not have to be unique. Note all entries are case sensitive.
    
    Once the unique username and password is entered the data is stored in the database.
    
    When the user tries to login, username and corresponding password needs to be entered. To
    gain access the password and username needs to be the same as the one stored in the database.
    Otherwise the system will not allow the user in.

How to run:

    To run the Application simply open Command Line Interface (CMD)/Console/Terminal
    and navigate to the root of the application, then type the command "python login.py" 
    or "login.py" the application will pop up.
    
    Once loaded the menu will pop up
    
    [ LOGIN SYSTEM ]
    [0] EXIT
    [1] LOGIN
    [2] SIGN UP
    
    You enter 1 to login, 2 to sign up or 0 to exit. 
    You simply follow the corrisponding number to the desired option it is that simple.

Components:

    The Application is made of four functions (menu, login, signup and insert). These
    all work together to make the Application run smoothly. When selected the desired
    option in the menu the correct function is selected in the while loop.
    
    The database 'users.db' is also a key component because it is needed for
    verification and storing data.

Built with:

    Python
    SQLite
    
Testing

    The following user was added in the database for testing purposes
    username: Athenkosi                 username: Luke
    password: zono12                    password: george        