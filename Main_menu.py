from New_registration import Registration
from Donor_login import Donor
from Receiver_login import receiver_login

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
            Registration().register()
        elif choice == '2':
            Donor().make_donation()
        elif choice == '3':
            receiver_login()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
