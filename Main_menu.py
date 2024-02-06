# from Donor_login import DonorLogin

# class Menu:
#     @staticmethod
#     def display():
#         print("Main Menu:")
#         print("1. New Registration")
#         print("2. Donor Login")
#         print("3. Exit")

# def main():
#     while True:
#         Menu.display()
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             print("Functionality for new registration")  # Placeholder for new registration functionality
#         elif choice == '2':
#             DonorLogin.donor_login()
#         elif choice == '3':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
# if __name__ == "__main__":
#     # Check if the user is registered or not
#     user_name = input("Enter your name: ")
#     if user_name not in donor:
#         print("User not registered. Please register as a donor.")
#         register_donor()

#     # Log in as a Donor
#     donor_login()

#     # Donate Food Items
#     donate_food()

#     # View Donation History
#     view_donation_history()


# # Dummy data storage
# volunteers = []
# donors = []
# ngos = [{'name': 'MyNGO', 'email': 'ngo@example.com', 'contact_no': '1234567890', 'password': '123', 'received_donations': []}]
# logged_in_user = None
# donation_history = []
# booked_items = []

# def register_user(user_type):
#     """Register as a volunteer, donor, or NGO."""
#     print(f"Register as a {user_type.capitalize()}:")
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     contact_no = input("Enter your contact number: ")
#     password = input("Choose a password: ")

#     user = {'name': name, 'email': email, 'contact_no': contact_no, 'password': password, 'donated_items': []}
    
#     if user_type == 'donor':
#         donors.append(user)
#     elif user_type == 'ngo':
#         ngos.append({'name': name, 'email': email, 'contact_no': contact_no, 'password': password, 'received_donations': []})
#     else:
#         volunteers.append(user)

#     print(f"{user_type.capitalize()} registered successfully!")

# def user_login(user_type):
#     """Log in as a donor or NGO."""
#     global logged_in_user
#     print(f"{user_type.capitalize()} Log in:")
#     name = input("Enter your name: ")
#     password = input("Enter your password: ")

#     if user_type == 'donor':
#         users = donors
#     elif user_type == 'ngo':
#         users = ngos
#     else:
#         users = volunteers

#     user = next((u for u in users if u['name'] == name and u['password'] == password), None)

#     if user:
#         logged_in_user = user
#         print("Login successful!")
#     else:
#         print("Invalid credentials. Login failed.")

# def donate_food():
#     """Donate food items."""
#     global logged_in_user, donation_history
#     if logged_in_user:
#         print("Donate Food Items:")
#         items = input("Enter food items to donate: ")
#         location = input("Enter donation location: ")

#         donation = {'donor': logged_in_user['name'], 'items': items, 'location': location}
#         donation_history.append(donation)

#         logged_in_user['donated_items'].append(donation)
#         print("Donation successful!")
#     else:
#         print("Please log in first.")

# def accept_or_reject_donations():
#     """Accept or reject donation requests."""
#     global logged_in_user, booked_items
#     if logged_in_user and 'ngo' in logged_in_user['name'].lower():
#         print("Accept/Reject Donations:")
#         for i, donation in enumerate(booked_items, 1):
#             print(f"{i}. Donor: {donation['donor']}, Items: {donation['items']}, Location: {donation['location']}")

#         choice = input("Enter the number of the donation to accept (or '0' to cancel): ")
#         if choice.isdigit() and 0 < int(choice) <= len(booked_items):
#             accepted_donation = booked_items.pop(int(choice) - 1)
#             logged_in_user['received_donations'].append(accepted_donation)
#             print("Donation accepted successfully!")
#         elif choice == '0':
#             print("Operation canceled.")
#         else:
#             print("Invalid choice.")

#     else:
#         print("Please log in as an NGO first.")

# def view_donation_history():
#     """View donation history."""
#     global logged_in_user
#     if logged_in_user:
#         print("View Donation History:")
#         for i, donation in enumerate(logged_in_user['donated_items'], 1):
#             print(f"{i}. Items: {donation['items']}, Location: {donation['location']}")
#     else:
#         print("Please log in first.")

# def view_received_donations():
#     """View received donations."""
#     global logged_in_user
#     if logged_in_user and 'ngo' in logged_in_user['name'].lower():
#         print("View Received Donations:")
#         for i, donation in enumerate(logged_in_user['received_donations'], 1):
#             print(f"{i}. Donor: {donation['donor']}, Items: {donation['items']}, Location: {donation['location']}")
#     else:
#         print("Please log in as an NGO first.")

# def main():
#     """Main function to orchestrate the flow."""
#     # Example usage:

#     # Check if the user is registered or not
#     user_name = input("Enter your name: ")
#     if any(user_name.lower() == donor['name'].lower() for donor in donors) or \
#        any(user_name.lower() == ngo['name'].lower() for ngo in ngos) or \
#        any(user_name.lower() == volunteer['name'].lower() for volunteer in volunteers):
#         print("User already registered. Please log in.")
#     else:
#         user_type = input("Enter user type (volunteer/donor/ngo): ")
#         if user_type.lower() in ['volunteer', 'donor', 'ngo']:
#             register_user(user_type)

#     # Log in
#     user_type = input("Enter user type to log in (volunteer/donor/ngo): ")
#     user_login(user_type)

#     # Donate or Accept/Reject Donations based on user type
#     if user_type.lower() == 'donor':
#         donate_food()
#         view_donation_history()
#     elif user_type.lower() == 'ngo':
#         accept_or_reject_donations()
#         view_received_donations()

# if __name__ == "__main__":
#     main()
from Donor_login import DonorLogin
from Receiver_login import ReceiverLogin
from New_registration import Registration
class Menu:
    def display(self):
        print("Main Menu:")
        print("1. New Registration")
        print("2. Donor Login")
        print("3. Receiver Login")
        print("4. Exit")

def main():
    menu = Menu()
    while True:
        menu.display()
        choice = input("Enter your choice: ")

        if choice == '1':
            Registration.register()
            print("Functionality for new registration")  # Placeholder for new registration functionality
        elif choice == '2':
            DonorLogin.donor_login()
        elif choice == '3':
            ReceiverLogin.receiver_login()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
