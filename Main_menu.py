from Donor_login import DonorLogin

class Menu:
    @staticmethod
    def display():
        print("Main Menu:")
        print("1. New Registration")
        print("2. Donor Login")
        print("3. Exit")

def main():
    while True:
        Menu.display()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Functionality for new registration")  # Placeholder for new registration functionality
        elif choice == '2':
            DonorLogin.donor_login()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
