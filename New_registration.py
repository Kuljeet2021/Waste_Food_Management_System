# # registered_users = {}
# # logged_in_users = set()
# # food_items = []

# # def register_user():
# #     print("New Registration")
# #     name = input("Enter your name: ")
# #     email = input("Enter your email: ")
# #     contact_no = input("Enter your contact number: ")
# #     address = input("Enter your address: ")
# #     password = input("Choose a password: ")

# #     new_user = {'name': name, 'email': email, 'contact_no': contact_no, 'address': address, 'password': password}

# #     # Store the user information in a dictionary using the user's name as the key.
# #     registered_users[name] = new_user
# #     return new_user

# # def user_login():
# #     name = input("Enter your name: ")
# #     password = input("Enter your password: ")

# #     user = registered_users.get(name)
# #     if user and user['password'] == password:
# #         logged_in_users.add(name)
# #         return True
# #     else:
# #         return False

# # def add_food_items():
# #     items = input("Enter food items (comma-separated): ")
# #     location = input("Enter location: ")
# #     quantity = int(input("Enter quantity: "))

# #     new_food_items = {'items': items, 'location': location, 'quantity': quantity}

# #     # Store the food items in a list.
# #     food_items.append(new_food_items)
# #     return new_food_items

# # def user_logout():
# #     name = input("Enter your name: ")
# #     if name in logged_in_users:
# #         logged_in_users.remove(name)

# # # Example usage:

# # # Register a user
# # user_info = register_user()
# # print("User registered:", user_info)

# # # Log in the user
# # login_successful = user_login()
# # print("Login successful:", login_successful)

# # # Add food items
# # food_info = add_food_items()
# # print("Food items added:", food_info)

# # # Log out the user
# # user_logout()
# # print("User logged out")

# # import mysql.connector

# # def connect_to_database():
# #     # Connect to MySQL database
# #     conn = mysql.connector.connect(
# #         host="localhost",
# #         user="root",  # Default username for XAMPP MySQL is 'root'
# #         password="",  # Default password is blank
# #         database="user_info"  # Replace 'user_info' with the name of your database
# #     )
# #     return conn

# # def create_table(conn):
# #     # Create a 'users' table if it doesn't exist
# #     cursor = conn.cursor()
# #     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
# #                         id INT AUTO_INCREMENT PRIMARY KEY,
# #                         name VARCHAR(255),
# #                         email VARCHAR(255)
# #                     )''')
# #     conn.commit()
# #     cursor.close()

# # def register_user(conn):
# #     name = input("Enter your name: ")
# #     email = input("Enter your email: ")

# #     cursor = conn.cursor()
# #     cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
# #     conn.commit()
# #     cursor.close()
# #     print("User registered successfully!")

# # def main():
# #     conn = connect_to_database()
# #     create_table(conn)

# #     register_user(conn)

# #     conn.close()

# # if __name__ == "__main__":
# #     main()

# donors = {}
# logged_in_donor = None
# donated_items = []

# def register_donor():
#     print("Register as a Donor:")
#     name = input("Enter your name: ")
#     email = input("Enter your email: ")
#     contact_no = input("Enter your contact number: ")
#     address = input("Enter your address: ")
#     password = input("Choose a password: ")

#     donor = {'name': name, 'email': email, 'contact_no': contact_no, 'address': address, 'password': password, 'donations': []}

#     # Store the donor information in a dictionary using the donor's name as the key.
#     donors[name] = donor
#     print("Donor registered successfully!")

# def donor_login():
#     global logged_in_donor
#     print("Donor Log in:")
#     name = input("Enter your name: ")

#     donor = donors.get(name)
#     if donor:
#         for attempt in range(3):
#             password = input("Enter your password: ")
#             if donor['password'] == password:
#                 logged_in_donor = donor
#                 print("Login successful!")
#                 return
#             else:
#                 print("Incorrect password. Attempts left:", 2 - attempt)
#         print("Too many incorrect attempts. Login failed.")
#     else:
#         print("Donor not found.")

# def donate_food():
#     global logged_in_donor
#     if logged_in_donor:
#         items = input("Enter food items to donate (comma-separated): ")
#         location = input("Enter donation location: ")
#         quantity = int(input("Enter quantity: "))

#         donation = {'donor': logged_in_donor['name'], 'items': items, 'location': location, 'quantity': quantity}
#         logged_in_donor['donations'].append(donation)
#         donated_items.append(donation)

#         print("Food items donated successfully!")
#     else:
#         print("Please log in first.")

# def view_donation_history():
#     global logged_in_donor
#     if logged_in_donor:
#         print("Donation History:")
#         for i, donation in enumerate(logged_in_donor['donations'], 1):
#             print(f"{i}. Items: {donation['items']}, Location: {donation['location']}, Quantity: {donation['quantity']}")
#     else:
#         print("Please log in first.")

# def logout():
#     global logged_in_donor
#     logged_in_donor = None
#     print("Logout successful!")

# # Volunteer Menu (for demonstration purposes)
# def volunteer_menu():
#     while True:
#         print("\nVolunteer Menu:")
#         print("1. View All Donated Items")
#         print("2. Exit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             if donated_items:
#                 print("\nAll Donated Items:")
#                 for i, donation in enumerate(donated_items, 1):
#                     print(f"{i}. Donor: {donation['donor']}, Items: {donation['items']}, Location: {donation['location']}, Quantity: {donation['quantity']}")
#                 else:
#                     print("No donated items available.")
#         elif choice == '2':
#             print("Exiting Volunteer Menu.")
#     else:
#         print("Invalid choice.")

# # Example usage:

# # Register as a Donor
# register_donor()

# # Log in as a Donor
# donor_login()

# # Donate Food
# donate_food()

# # View Donation History
# view_donation_history()

# # Logout
# logout()

# # Volunteer Menu
# volunteer_menu()


# class DonorLogin:
#     @staticmethod
#     def donor_login():
#         print("Donor Log in:")
#         name = input("Enter your name: ")
#         # Assuming the donors dictionary is defined in donor_login.py
#         donor = donors.get(name)
#         if donor:
#             password = input("Enter your password: ")
#             if donor['password'] == password:
#                 Menu.logged_in_donor = donor
#                 print("Login successful!")
#             else:
#                 print("Incorrect password.")
#         else:
#             print("Donor not found.")
class Registration:
    @staticmethod
    def register():
        print("New Registration")
        # Add your registration logic here
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Choose a password: ")
        # Add your registration process here
        print("User registered successfully!")
