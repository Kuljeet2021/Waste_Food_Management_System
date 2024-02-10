# import time

# class Donation:
#     def __init__(self, donor_name, contact_details, address, pickup_location, food_items):
#         self.donor_name = donor_name
#         self.contact_details = contact_details
#         self.address = address
#         self.pickup_location = pickup_location
#         self.food_items = food_items
#         self.timestamp = time.time()  # Timestamp when donation is made
#         self.picked_up = False

# class ReceiverLogin:
#     def __init__(self):
#         print("Receiver Login")
#         self.donations = []

#     def list_available_donations(self):
#         if not self.donations:
#             print("No donations available at the moment.")
#         else:
#             print("Available donations:")
#             for idx, donation in enumerate(self.donations):
#                 print(f"Donation {idx + 1}:")
#                 print(f"Food items: {donation['food_items']}")
#                 print(f"Time: {donation['time']}")
#                 print(f"Address: {donation['address']}")
#                 print()

#     def accept_donation(self, donation_index):
#         if donation_index < 1 or donation_index > len(self.donations):
#             print("Invalid donation index.")
#             return
#         decision = input("Do you want to accept this donation? (yes/no): ").lower()
#         if decision == "yes":
#             donation = self.donations[donation_index - 1]
#             self.send_notification(donation['food_items'], donation['time'], donation['address'])
#             print("Donation accepted successfully!")
#             del self.donations[donation_index - 1]
#         else:
#             print("Donation declined.")

#     def send_notification(self, food_items, time, address):
#         print("Notification sent to the donor: Donation accepted.")
#         print(f"Food items: {food_items}")
#         print(f"Time: {time}")
#         print(f"Address: {address}")

# def receiver_login():
#     receiver = ReceiverLogin()

#     # Adding some donations for demonstration
#     receiver.donations.append({"food_items": ["Bread", "Milk", "Fruits"], "time": "10:00 AM", "address": "123 Main St"})
#     receiver.donations.append({"food_items": ["Rice", "Vegetables"], "time": "12:00 PM", "address": "456 Elm St"})
    
#     # Listing available donations
#     receiver.list_available_donations()

#     # Receiver decides whether to accept or decline a donation
#     donation_index = int(input("Enter the index of the donation you want to accept: "))
#     receiver.accept_donation(donation_index)

#     # Listing available donations after accepting or declining
#     receiver.list_available_donations()

# if __name__ == "__main__":
#     receiver_login()


import time

class Donation:
    def __init__(self, donor_name, contact_details, address, pickup_location, food_items):
        self.donor_name = donor_name
        self.contact_details = contact_details
        self.address = address
        self.pickup_location = pickup_location
        self.food_items = food_items
        self.timestamp = time.time()  # Timestamp when donation is made
        self.picked_up = False

class ReceiverLogin:
    def __init__(self):
        print("Receiver Login")
        self.donations = []
    
    def list_available_donations(self):
        if not self.donations:
            print("No donations available at the moment.")
        else:
            print("Available donations:")
            for idx, donation in enumerate(self.donations):
                print(f"Donation {idx + 1}:")
                print(f"Food items: {donation['food_items']}")
                print(f"Time: {donation['time']}")
                print(f"Address: {donation['address']}")
                print()

    def accept_donation(self, donation_index):
        if donation_index < 1 or donation_index > len(self.donations):
            print("Invalid donation index.")
            return
        decision = input("Do you want to accept this donation? (yes/no): ").lower()
        if decision == "yes":
            donation = self.donations[donation_index - 1]
            self.send_notification(donation['food_items'], donation['time'], donation['address'])
            print("Donation accepted successfully!")
            del self.donations[donation_index - 1]
        else:
            print("Donation declined.")
    
    def send_notification(self, food_items, time, address):
        print("Notification sent to the donor: Donation accepted.")
        print(f"Food items: {food_items}")
        print(f"Time: {time}")
        print(f"Address: {address}")

def receiver_login():
    receiver = ReceiverLogin()
    
    # Adding some donations for demonstration
    receiver.donations.append({"food_items": ["Bread", "Milk", "Fruits"], "time": "10:00 AM", "address": "123 Main St"})
    receiver.donations.append({"food_items": ["Rice", "Vegetables"], "time": "12:00 PM", "address": "456 Elm St"})
    
    # Listing available donations
    receiver.list_available_donations()
    
    # Receiver decides whether to accept or decline a donation
    donation_index = int(input("Enter the index of the donation you want to accept: "))
    receiver.accept_donation(donation_index)
    
    # Listing available donations after accepting or declining
    receiver.list_available_donations()

if __name__ == "__main__":
    receiver_login()
