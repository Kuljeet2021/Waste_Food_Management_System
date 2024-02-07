import time

class Donation:
    def __init__(self, donor_name, contact_details, address, pickup_location, food_items):
        self.donor_name = donor_name
        self.contact_details = contact_details
        self.address = address
        self.pickup_location = pickup_location
        self.food_items = food_items
        self.timestamp = time.time()
        self.picked_up = False

class Donor:
    def __init__(self):
        self.donations = []

    def make_donation(self):
        donor_name = input("Enter your name: ")
        contact_details = input("Enter your contact details: ")
        address = input("Enter your address: ")
        pickup_location = input("Enter the pickup location: ")
        food_items = input("Enter the food items (comma-separated): ").split(",")

        donation = Donation(donor_name, contact_details, address, pickup_location, food_items)
        self.donations.append(donation)
        print("Donation added successfully!")
        self.check_pickup(donation)

    def check_pickup(self, donation):
        print(f"Waiting for pickup at {donation.pickup_location}...")
        time.sleep(20)
        if not donation.picked_up:
            print("No one came to pick up the donation. Would you like to cancel it?")
            decision = input("Enter 'yes' to cancel or 'no' to keep waiting: ").lower()
            if decision == "yes":
                self.cancel_donation(donation)
            else:
             print("We'll continue waiting for pickup.")

    def cancel_donation(self, donation):
        self.donations.remove(donation)
        print("Donation canceled successfully.")
    
    



    def show_donation_history(self):
        if not self.donations:
            print("You haven't made any donations yet.")
        else:
            print("Donation history:")
            for idx, donation in enumerate(self.donations):
                status = "Picked up" if donation.picked_up else "Not picked up"
                print(f"Donation {idx + 1}:")
                print(f"Donor Name: {donation.donor_name}")
                print(f"Contact Details: {donation.contact_details}")
                print(f"Address: {donation.address}")
                print(f"Pickup Location: {donation.pickup_location}")
                print(f"Food Items: {donation.food_items}")
                print(f"Status: {status}")
                print()

