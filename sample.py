
donors = {}
logged_in_donor = None
donated_items = []

def register_donor():
    print("Register as a Donor:")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    contact_no = input("Enter your contact number: ")
    address = input("Enter your address: ")
    password = input("Choose a password: ")

    donor = {'name': name, 'email': email, 'contact_no': contact_no, 'address': address, 'password': password, 'donations': []}

    # Store the donor information in a dictionary using the donor's name as the key.
    donors[name] = donor
    print("Donor registered successfully!")

def donor_login():
    global logged_in_donor
    print("Donor Log in:")
    name = input("Enter your name: ")

    donor = donors.get(name)
    if donor:
        for attempt in range(3):
            password = input("Enter your password: ")
            if donor['password'] == password:
                logged_in_donor = donor
                print("Login successful!")
                return
            else:
                print("Incorrect password. Attempts left:", 2 - attempt)
        print("Too many incorrect attempts. Login failed.")
    else:
        print("Donor not found.")

def donate_food():
    global logged_in_donor
    if logged_in_donor:
        items = input("Enter food items to donate (comma-separated): ")
        location = input("Enter donation location: ")
        quantity = int(input("Enter quantity: "))

        donation = {'donor': logged_in_donor['name'], 'items': items, 'location': location, 'quantity': quantity}
        logged_in_donor['donations'].append(donation)
        donated_items.append(donation)

        print("Food items donated successfully!")
    else:
        print("Please log in first.")

def view_donation_history():
    global logged_in_donor
    if logged_in_donor:
        print("Donation History:")
        for i, donation in enumerate(logged_in_donor['donations'], 1):
            print(f"{i}. Items: {donation['items']}, Location: {donation['location']}, Quantity: {donation['quantity']}")
    else:
        print("Please log in first.")

def logout():
    global logged_in_donor
    logged_in_donor = None
    print("Logout successful!")

# Volunteer Menu (for demonstration purposes)
def volunteer_menu():
    while True:
        print("\nVolunteer Menu:")
        print("1. View All Donated Items")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            if donated_items:
                print("\nAll Donated Items:")
                for i, donation in enumerate(donated_items, 1):
                    print(f"{i}. Donor: {donation['donor']}, Items: {donation['items']}, Location: {donation['location']}, Quantity: {donation['quantity']}")
                else:
                    print("No donated items available.")
        elif choice == '2':
            print("Exiting Volunteer Menu.")
    else:
        print("Invalid choice.")

# Example usage:

# Register as a Donor
register_donor()

# Log in as a Donor
donor_login()

# Donate Food
donate_food()

# View Donation History
view_donation_history()

# Logout
logout()

# Volunteer Menu
volunteer_menu()