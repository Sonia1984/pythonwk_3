from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register 


#Declared variables, user will be logged in
database = {"admin":"password123", "Mary": "1234", "Bob": "1234"}
donations = ["donation_string"]
authorized_user = ""
show_homepage()
if authorized_user == "":
        print("You must be logged in to donate")
elif authorized_user != "":
        print("Logged in as:admin", authorized_user)
options =(input("Please choose from the following options: "))
if options == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(database,username, password)
# The user is then given options to choose from  
elif options == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register(database, username)
        if authorized_user != "":
           database["username"] = password
elif options == "3":
        if authorized_user == "":
               print("You are not logged in")
        donation_string = donate(authorized_user)
elif options == "4":
        show_donations(donations)
elif options == "5":
        print("Goodbye!, Thank you for your donation")





