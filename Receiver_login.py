class ReceiverLogin:
    @staticmethod
    def receiver_login():
        print("Receiver Login")
        # Add your receiver login logic here
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        # Add your authentication logic here
        if name == "example_receiver" and password == "password":
            print("Login successful!")
        else:
            print("Invalid credentials. Login failed.")
