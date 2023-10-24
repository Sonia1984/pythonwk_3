#This is the functionality behind how users interact with the database
def login(database, username, password):
     if username in database and database[username] == password:
        print("Welcome", username)
        print("Welcome to DonationMe")
     else:
        print("Invalid username or password")
def register(database, username):
    if username in database:
        print("Username already registered")
        return()
    else:
        print("User name has been registered")
        return(username)
       

    
   
    


    
