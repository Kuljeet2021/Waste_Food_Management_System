# import mysql.connector

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.food_items = []

#     def create_food_item(self, quantity, location, address, contact):
#         cursor.execute("INSERT INTO food_items (quantity, location, address, contact, user_id) VALUES (%s, %s, %s, %s, %s)",
#                        (quantity, location, address, contact, self.id))
#         connection.commit()

#     def display_food_items(self):
#         cursor.execute("SELECT * FROM food_items WHERE user_id = %s", (self.id,))
#         for row in cursor.fetchall():
#             print(f"Quantity: {row[1]}, Location: {row[2]}, Address: {row[3]}, Contact: {row[4]}")

# # Connect to MySQL
# connection = mysql.connector.connect(
#     host='localhost',
#     user='your_username',
#     password='your_password',
#     database='food_donation_system'
# )

# cursor = connection.cursor()

# # Create tables if not exists
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         username VARCHAR(20) UNIQUE NOT NULL,
#         password VARCHAR(60) NOT NULL
#     )
# """)

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS food_items (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         quantity INT NOT NULL,
#         location VARCHAR(100) NOT NULL,
#         address VARCHAR(200) NOT NULL,
#         contact VARCHAR(15) NOT NULL,
#         user_id INT,
#         FOREIGN KEY (user_id) REFERENCES users(id)
#     )
# """)

# connection.commit()

# def main():
#     # Example usage
#     user = User("donor123", "password123")

#     # Donor creates a food item
#     user.create_food_item(quantity=5, location="City Center", address="123 Main St", contact="123-456-7890")

#     # Donor displays their food items
#     user.display_food_items()

# if __name__ == '__main__':
#     main()

#############  user reg ###############
from Main_menu import Menu
from user import User

registered_users = {}
logged_in_users = set()
food_items = []

def register_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    contact_no = input("Enter your contact number: ")
    address = input("Enter your address: ")
    password = input("Choose a password: ")

    new_user = {'name': name, 'email': email, 'contact_no': contact_no, 'address': address, 'password': password}

    # Store the user information in a dictionary using the user's name as the key.
    registered_users[name] = new_user
    return new_user

def user_login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    user = registered_users.get(name)
    if user and user['password'] == password:
        logged_in_users.add(name)
        return True
    else:
        return False

def add_food_items():
    items = input("Enter food items (comma-separated): ")
    location = input("Enter location: ")
    quantity = int(input("Enter quantity: "))

    new_food_items = {'items': items, 'location': location, 'quantity': quantity}

    # Store the food items in a list.
    food_items.append(new_food_items)
    return new_food_items

def user_logout():
    name = input("Enter your name: ")
    if name in logged_in_users:
        logged_in_users.remove(name)

# Example usage:

# Register a user
user_info = register_user()
print("User registered:", user_info)

# Log in the user
login_successful = user_login()
print("Login successful:", login_successful)

# Add food items
food_info = add_food_items()
print("Food items added:", food_info)

# Log out the user
user_logout()
print("User logged out")