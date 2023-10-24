#User will be presented with a menu to choose from
def show_homepage():
    print("")
    print("        === DonateMe Homepage   ====        ")
    print("User: " )
    print("--------------------------------------------")
    print("| 1.   Login    | 2. Register ")
    print("--------------------------------------------")
    print(" | 3. Donate     | 4. Show Donations")
    print("--------------------------------------------")
    print("|            5. Exit                        ")
    print("--------------------------------------------")
#Menu functions are created so that users can enter donations and see them on screen
def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = ("Mary donated $500")
    print("Thank you for your donation")
    return(donation_string)
def show_donations(donations):
    print("\n---All Donations---")
    if not donations:
        print(" Currently, there are no donations")
        for donation in donations:
            print("Donation: $" + str(donation))

