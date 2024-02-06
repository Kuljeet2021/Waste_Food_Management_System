# volunteers = {}
# donors = {}
# logged_in_volunteer = None
# logged_in_donor = None
# booked_items = []
# donation_history = []

# def register_volunteer():
#     """Register as a volunteer."""
#     # ...

# def register_donor():
#     """Register as a donor."""
#     print("Register as a Donor:")
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     contact_no = input("Enter your contact number: ")
#     password = input("Choose a password: ")

#     donor = {'name': name, 'email': email, 'contact_no': contact_no, 'password': password, 'donated_items': []}

#     donors[name] = donor
#     print("Donor registered successfully!")

# def donor_login():
#     """Log in as a donor."""
#     global logged_in_donor
#     print("Donor Log in:")
#     name = input("Enter your name: ")
#     password = input("Enter your password: ")

#     donor = donors.get(name)
#     if donor and donor['password'] == password:
#         logged_in_donor = donor
#         print("Login successful!")
#     else:
#         print("Invalid credentials. Login failed.")

# def donate_food():
#     """Donate food items."""
#     global logged_in_donor, donation_history
#     if logged_in_donor:
#         print("Donate Food Items:")
#         items = input("Enter food items to donate: ")
#         location = input("Enter donation location: ")

#         donation = {'donor': logged_in_donor['name'], 'items': items, 'location': location}
#         donation_history.append(donation)

#         logged_in_donor['donated_items'].append(donation)
#         print("Donation successful!")
#     else:
#         print("Please log in first.")

# def view_donation_history():
#     """View donation history."""
#     global logged_in_donor
#     if logged_in_donor:
#         print("View Donation History:")
#         for i, donation in enumerate(logged_in_donor['donated_items'], 1):
#             print(f"{i}. Items: {donation['items']}, Location: {donation['location']}")
#     else:
#         print("Please log in first.")

# def main():
#     """Main function to orchestrate the flow."""
#     # ...

# # Example usage:
# if __name__ == "_main_":
#     # Check if the user is registered or not
#     user_name = input("Enter your name: ")
#     if user_name not in donors:
#         print("User not registered. Please register as a donor.")
#         register_donor()

#     # Log in as a Donor
#     donor_login()

#     # Donate Food Items
#     donate_food()

#     # View Donation History
#     view_donation_history()


# class DonorLogin:
#     @staticmethod
#     def donor_login():
#         print("Donor Login")
#         # Add your donor login logic here
#         name = input("Enter your name: ")
#         password = input("Enter your password: ")
#         # Add your authentication logic here
#         if name == "Abhang karode" and password == "Abhang09@":
#             print("Login successful!")
#         else:
#             print("Invalid credentials. Login failed.")


class DonorLogin:
    def __init__(self):
        self.users = {
            "Abhang karode": "Abhang09@"
            # Add more user credentials here if needed
        }

    def donor_login(self):
        print("Donor Login")
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name in self.users and self.users[name] == password:
            print("Login successful!")
        else:
            print("Invalid credentials. Login failed.")