import json
import os
import unittest
import argparse
import sys


# Constants for default file paths
HOTEL_FILE = "hotels.json"
CUSTOMER_FILE = "customers.json"
RESERVATION_FILE = "reservations.json"


class Hotel:
    def __init__(self, hotel_id, name, address, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.address = address
        self.rooms = rooms  # Dictionary: {room_number: price}

    def display_info(self):
        print(f"Hotel ID: {self.hotel_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print("Rooms:")
        for room, price in self.rooms.items():
            print(f"  Room {room}: ${price}")


class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")


class Reservation:
    def __init__(self, reservation_id, customer_id, hotel_id, room_number, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def display_info(self):
        print(f"Reservation ID: {self.reservation_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Hotel ID: {self.hotel_id}")
        print(f"Room Number: {self.room_number}")
        print(f"Check-in: {self.check_in_date}")
        print(f"Check-out: {self.check_out_date}")


# --- Data Persistence Functions ---

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filename}. Data may be corrupted.")
        return {}


def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# --- Hotel Management ---

def create_hotel(hotel_data):
    hotels = load_data(HOTEL_FILE)
    if hotel_data['hotel_id'] in hotels:
        print("Error: Hotel with this ID already exists.")
        return
    hotels[hotel_data['hotel_id']] = hotel_data
    save_data(hotels, HOTEL_FILE)


def delete_hotel(hotel_id):
    hotels = load_data(HOTEL_FILE)
    if hotel_id not in hotels:
        print("Error: Hotel with this ID does not exist.")
        return
    del hotels[hotel_id]
    save_data(hotels, HOTEL_FILE)


def display_hotel_info(hotel_id):
    hotels = load_data(HOTEL_FILE)
    if hotel_id not in hotels:
        print("Error: Hotel with this ID does not exist.")
        return
    hotel = Hotel(**hotels[hotel_id])  # Create Hotel object
    hotel.display_info()


def modify_hotel_info(hotel_id, updated_data):
    hotels = load_data(HOTEL_FILE)
    if hotel_id not in hotels:
        print("Error: Hotel with this ID does not exist.")
        return
    hotels[hotel_id].update(updated_data)  # Update existing data
    save_data(hotels, HOTEL_FILE)


def reserve_room(hotel_id, room_number):
    hotels = load_data(HOTEL_FILE)
    if hotel_id not in hotels:
        print("Error: Hotel with this ID does not exist.")
        return
    if room_number not in hotels[hotel_id]['rooms']:
        print("Error: Room number does not exist in this hotel")
        return
    print(f"Room {room_number} reserved in Hotel {hotel_id}")  # Placeholder


def cancel_reservation_hotel(hotel_id, room_number):
    hotels = load_data(HOTEL_FILE)
    if hotel_id not in hotels:
        print("Error: Hotel with this ID does not exist.")
        return
    if room_number not in hotels[hotel_id]['rooms']:
        print("Error: Room number does not exist in this hotel")
        return
    print(f"Reservation for Room {room_number} in Hotel {hotel_id} cancelled")  # Placeholder


# --- Customer Management ---

def create_customer(customer_data):
    customers = load_data(CUSTOMER_FILE)
    if customer_data['customer_id'] in customers:
        print("Error: Customer with this ID already exists.")
        return
    customers[customer_data['customer_id']] = customer_data
    save_data(customers, CUSTOMER_FILE)


def delete_customer(customer_id):
    customers = load_data(CUSTOMER_FILE)
    if customer_id not in customers:
        print("Error: Customer with this ID does not exist.")
        return
    del customers[customer_id]
    save_data(customers, CUSTOMER_FILE)


def display_customer_info(customer_id):
    customers = load_data(CUSTOMER_FILE)
    if customer_id not in customers:
        print("Error: Customer with this ID does not exist.")
        return
    customer = Customer(**customers[customer_id])
    customer.display_info()


def modify_customer_info(customer_id, updated_data):
    customers = load_data(CUSTOMER_FILE)
    if customer_id not in customers:
        print("Error: Customer with this ID does not exist.")
        return
    customers[customer_id].update(updated_data)
    save_data(customers, CUSTOMER_FILE)


# --- Reservation Management ---

def create_reservation(reservation_data):
    reservations = load_data(RESERVATION_FILE)
    if reservation_data['reservation_id'] in reservations:
        print("Error: Reservation with this ID already exists.")
        return

    reservations[reservation_data['reservation_id']] = reservation_data
    save_data(reservations, RESERVATION_FILE)


def cancel_reservation(reservation_id):
    reservations = load_data(RESERVATION_FILE)
    if reservation_id not in reservations:
        print("Error: Reservation with this ID does not exist.")
        return
    del reservations[reservation_id]
    save_data(reservations, RESERVATION_FILE)


# --- Command-line argument parsing ---
def parse_arguments():
    parser = argparse.ArgumentParser(description="Hotel Reservation System")
    parser.add_argument("--hotels", help="Path to the hotels JSON file", default=HOTEL_FILE)
    parser.add_argument("--customers", help="Path to the customers JSON file", default=CUSTOMER_FILE)
    parser.add_argument("--reservations", help="Path to the reservations JSON file", default=RESERVATION_FILE)
    return parser.parse_args()


# --- Unit Tests ---

class TestHotel(unittest.TestCase):
    def setUp(self):
        args = parse_arguments()
        self.hotel_file = args.hotels
        self.test_hotel_data = {"1": {"hotel_id": "1", "name": "Test Hotel", "address": "Test Address",
                                      "rooms": {"101": 100, "102": 150}}}
        save_data(self.test_hotel_data, self.hotel_file)

    def tearDown(self):
        try:
            os.remove(self.hotel_file)
        except FileNotFoundError:
            pass

    def test_create_hotel(self):
        new_hotel_data = {"2": {"hotel_id": "2", "name": "New Hotel", "address": "New Address", "rooms": {"201": 200}}}
        create_hotel(new_hotel_data["2"])  # Correct: Pass the value, not the entire dictionary
        loaded_data = load_data(self.hotel_file)
        self.assertIn("2", loaded_data)
        self.assertEqual(loaded_data["2"]["name"], "New Hotel")

    def test_delete_hotel(self):
        delete_hotel("1")
        loaded_data = load_data(self.hotel_file)
        self.assertNotIn("1", loaded_data)

    def test_display_hotel_info(self):
        # Capture stdout to check printed output (more robust way to test print)
        import io
        import sys
        captured_out = io.StringIO()
        sys.stdout = captured_out
        display_hotel_info("1")
        sys.stdout = sys.__stdout__  # reset stdout
        self.assertIn("Test Hotel", captured_out.getvalue())  # Check if hotel name is printed.

    def test_modify_hotel_info(self):
        updated_data = {"name": "Updated Hotel Name", "address": "Updated Address"}
        modify_hotel_info("1", updated_data)
        loaded_data = load_data(self.hotel_file)
        self.assertEqual(loaded_data["1"]["name"], "Updated Hotel Name")
        self.assertEqual(loaded_data["1"]["address"], "Updated Address")

    def test_reserve_room(self):
        reserve_room("1", "101")  # Just a basic test, expand as needed.

    def test_cancel_reservation_hotel(self):
        cancel_reservation_hotel("1", "101")  # Basic test.


# --- Main execution block ---
# ... (imports, classes, functions remain the same)

if __name__ == '__main__':
    args = parse_arguments()
    HOTEL_FILE = args.hotels
    CUSTOMER_FILE = args.customers
    RESERVATION_FILE = args.reservations

    # 1. Create a TestSuite
    suite = unittest.TestSuite()

    # 2. Discover tests automatically (recommended):
    loader = unittest.TestLoader()
    suite.addTests(loader.discover(start_dir=".", pattern="test*.py"))  # Discover tests in current directory.

    # 3. Run the tests:
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if not result.wasSuccessful():
        sys.exit(1)  # Indicate test failure
    else:
        sys.exit(0)   # Indicate test success
