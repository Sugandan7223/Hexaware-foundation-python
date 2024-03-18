import pyodbc
from abc import ABC, abstractmethod
from datetime import datetime
import os


class AdoptionException(Exception):
    pass


class InvalidPetAgeException(Exception):
    pass


class FileHandlingException(Exception):
    pass


class NullReferenceException(Exception):
    pass


class DatabaseOperationException(Exception):
    pass

class IAdoptable(ABC):
    @abstractmethod
    def Adopt(self):
        pass

def connect_to_sql_server():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-A08GADU\SQLEXPRESS01;'
                              'Database=PetPals;'
                              'Trusted_Connection=yes;')
        print("Connected Successfully")
        return conn
    except pyodbc.Error as ex:
        print(f"Error: {ex}")


def close_connection(conn):
    conn.close()
    print("Connection closed.")


class Pet:
    def __init__(self, pet_id, name, age, breed, pet_type, available_for_adoption, shelter_name, owner_id, shelter_id):
        self.pet_id = pet_id
        self.name = name
        self.age = age
        self.breed = breed
        self.pet_type = pet_type
        self.available_for_adoption = available_for_adoption
        self.shelter_name = shelter_name
        self.owner_id = owner_id
        self.shelter_id = shelter_id

    def get_pet_id(self):
        return self._pet_id

    def set_pet_id(self, pet_id):
        self._pet_id = pet_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def get_pet_type(self):
        return self._pet_type

    def set_pet_type(self, pet_type):
        self._pet_type = pet_type

    def is_available_for_adoption(self):
        return self._available_for_adoption

    def set_available_for_adoption(self, available_for_adoption):
        self._available_for_adoption = available_for_adoption

    def get_shelter_name(self):
        return self._shelter_name

    def set_shelter_name(self, shelter_name):
        self._shelter_name = shelter_name

    def get_owner_id(self):
        return self._owner_id

    def set_owner_id(self, owner_id):
        self._owner_id = owner_id

    def get_shelter_id(self):
        return self._shelter_id

    def set_shelter_id(self, shelter_id):
        self._shelter_id = shelter_id

    def Adopt(self):
        try:
        
            print(f"Adoption process handled for pet {self._name}")
        except Exception as e:
            raise AdoptionException(f"Error handling adoption: {e}")

    def __str__(self):
        try:
            return f"{self.name}, {self.age}, {self.breed}, {self.pet_type}, {self.available_for_adoption}, {self.shelter_name}, {self.owner_id}, {self.shelter_id}"
        except AttributeError:
            raise NullReferenceException("Pet information is missing.")


class Dog(Pet):
    def __init__(self, pet_id, name, age, breed, pet_type, available_for_adoption, shelter_name, owner_id, shelter_id,
                 dog_breed):
        super().__init__(pet_id, name, age, breed, pet_type, available_for_adoption, shelter_name, owner_id, shelter_id)
        self.dog_breed = dog_breed

    def get_dog_breed(self):
        return self.dog_breed

    def set_dog_breed(self, dog_breed):
        self.dog_breed = dog_breed


class Cat(Pet):
    def __init__(self, pet_id, name, age, breed, pet_type, available_for_adoption, shelter_name, owner_id, shelter_id,
                 cat_color):
        super().__init__(pet_id, name, age, breed, pet_type, available_for_adoption, shelter_name, owner_id, shelter_id)
        self.cat_color = cat_color

    def get_cat_color(self):
        return self.cat_color

    def set_cat_color(self, cat_color):
        self.cat_color = cat_color


class PetShelter:
    def __init__(self):
        self.available_pets = []

    def add_pet(self, pet):
        self.available_pets.append(pet)

    def remove_pet(self, pet):
        self.available_pets.remove(pet)

    def list_available_pets(self):
        if not self.available_pets:
            print("No pets available for adoption.")
        else:
            print("Available Pets:")
            for pet in self.available_pets:
                try:
                    print(pet)
                except NullReferenceException as nre:
                    print(f"Error: {nre}")
                    continue


class AdoptionEvent:
    def __init__(self, event_id, event_name, event_date, location, city, organizer_id):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.city = city
        self.organizer_id = organizer_id

    def __str__(self):
        return f"Event ID: {self.event_id}, Name: {self.event_name}, Date: {self.event_date}, Location: {self.location}"

    def HostEvent(self):
        print("Adoption event hosted successfully.")

class AdoptionEventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def list_events(self):
        if not self.events:
            print("No upcoming adoption events.")
        else:
            print("Upcoming Adoption Events:")
            for event in self.events:
                print(event)

class Participant:
    def __init__(self, participant_id, participant_name, participant_email, event_id, city):
        self.participant_id = participant_id
        self.participant_name = participant_name
        self.participant_email = participant_email
        self.event_id = event_id
        self.city = city

    def __str__(self):
        return f"Participant ID: {self.participant_id}, Name: {self.participant_name}, Email: {self.participant_email}, Event ID: {self.event_id}, City: {self.city}"




    def add_participant(self, participant):
        self.participants_list.append(participant)

    def remove_participant(self, participant):
        self.participants_list.remove(participant)

    def list_participants(self):
        if not self.participants_list:
            print("No participants registered.")
        else:
            print("Registered Participants:")
            for participant in self.participants_list:
                try:
                    print(participant)
                except NullReferenceException as nre:
                    print(f"Error: {nre}")
                    continue
class PList:
    def __init__(self):
        self.participants_list = []

    @classmethod
    def create_instance(cls):
        return cls()

    def add_participant(self, participant):
        self.participants_list.append(participant)

    def remove_participant(self, participant):
        self.participants_list.remove(participant)

    def list_participants(self):
        if not self.participants_list:
            print("No participants registered.")
        else:
            print("Registered Participants:")
            for participant in self.participants_list:
                try:
                    print(participant)
                except NullReferenceException as nre:
                    print(f"Error: {nre}")
                    continue

class Database:
    def __init__(self):
        self.conn = connect_to_sql_server()

    def get_available_pets(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Pets")
            pets = cursor.fetchall()
            return pets
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return []

    def get_upcoming_events(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM AdoptionEvents WHERE EventDate >= ?", datetime.now())
            events = cursor.fetchall()
            return events
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return []

    def register_participant(self, participant_id, participant_name, participant_email, event_id, city):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Participants (ParticipantID, ParticipantName, ParticipantType,EventID,City) VALUES (?, ?, ?,?,?)",
                (participant_id, participant_name, participant_email, event_id, city))
            self.conn.commit()
            print("Participant registered successfully.")
        except pyodbc.Error as ex:
            print(f"Error registering participant: {ex}")
            raise DatabaseOperationException("Failed to register participant.")

    def retrieve_all_participants(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Participants")
            pets = cursor.fetchall()
            return pets
        except pyodbc.Error as ex:
                    print(f"Error: {ex}")
                    return []


class Donation(ABC):
    def __init__(self, donation_id, donor_name, donation_type, donation_amount, donation_item, donation_date,
                 shelter_id):
        self.donation_id = donation_id
        self.donor_name = donor_name
        self.donation_type = donation_type
        self.donation_amount = donation_amount
        self.donation_item = donation_item
        self.donation_date = donation_date
        self.shelter_id = shelter_id

    @abstractmethod
    def record_donation(self):
        pass


class CashDonation(Donation):
    def record_donation(self):
        try:
            cursor = db.conn.cursor()
            cursor.execute(
                "INSERT INTO Donations (DonationID,DonorName, DonationType, DonationAmount, DonationItem, DonationDate, ShelterID) VALUES (?,?, ?, ?, ?, ?, ?)",
                (self.donation_id, self.donor_name, self.donation_type, self.donation_amount, None, self.donation_date,
                 self.shelter_id))
            db.conn.commit()
            print(f"Cash donation of ${self.donation_amount} recorded on {self.donation_date} by {self.donor_name}")
        except pyodbc.Error as ex:
            print(f"Error recording cash donation: {ex}")


class ItemDonation(Donation):
    def record_donation(self):
        try:
            cursor = db.conn.cursor()
            cursor.execute(
                "INSERT INTO Donations (DonationID,DonorName, DonationType, DonationAmount, DonationItem, DonationDate, ShelterID) VALUES (?,?, ?, ?, ?, ?, ?)",
                (self.donation_id, self.donor_name, self.donation_type, self.donation_amount, self.donation_item,
                 self.donation_date, self.shelter_id))
            db.conn.commit()
            print(f"Item donation of {self.donation_item} worth ${self.donation_amount} recorded by {self.donor_name}")
        except pyodbc.Error as ex:
            print(f"Error recording item donation: {ex}")


def display_menu():
    print("1. List Available Pets")
    print("2. Record Cash Donation")
    print("3. Record Item Donation")
    print("4. List Upcoming Adoption Events")
    print("5. Register for an Adoption Event")
    print("6. Read Data from File")
    print("7. Read all Participants")
    print("8. Exit")


def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        raise FileHandlingException("File not found.")
    except IOError:
        raise FileHandlingException("Error reading file.")


if __name__ == "__main__":

    db = Database()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":

            shelter = PetShelter()

            pets = db.get_available_pets()
            for pet in pets:
                shelter.add_pet(Pet(*pet))

            shelter.list_available_pets()
        elif choice == "2":
            try:
                donation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                donation_id = input("Enter donation ID: ")
                donor_name = input("Enter donor name: ")
                donation_amount = float(input("Enter donation amount: "))
                cash_donation = CashDonation(donation_id, donor_name, "Cash", donation_amount, None, donation_date, 1)
                cash_donation.record_donation()
            except ValueError as ve:
                print(f"Error: {ve}")
        elif choice == "3":
            try:
                donation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                donation_id = input("Enter donation ID: ")
                donor_name = input("Enter donor name: ")
                donation_amount = float(input("Enter donation amount: "))
                donation_item = input("Enter donation item: ")
                item_donation = ItemDonation(donation_id, donor_name, "Item", donation_amount, donation_item,
                                             donation_date, 1)
                item_donation.record_donation()
            except ValueError as ve:
                print(f"Error: {ve}")
        elif choice == "4":

            try:
                events = db.get_upcoming_events()
                event_manager = AdoptionEventManager()
                for event in events:
                    event_manager.add_event(AdoptionEvent(*event))
                event_manager.list_events()
            except DatabaseOperationException as doe:
                print(f"Database Operation Error: {doe}")
        elif choice == "5":
            try:
                participant_id = input("Enter your ID : ")
                event_id = input("Enter event ID to register for: ")
                participant_name = input("Enter your name: ")
                participant_email = input("Enter your email: ")
                city = input("Enter event City: ")
                db.register_participant(participant_id, participant_name, participant_email, event_id, city)
            except DatabaseOperationException as doe:
                print(f"Database Operation Error: {doe}")
        elif choice == "6":
            try:
                file_name = input("Enter the file name: ")
                file_path = os.path.join(os.getcwd(), file_name)
                data = read_data_from_file(file_path)
                print("Data read successfully:")
                print(data)
            except FileHandlingException as fe:
                print(f"File Handling Error: {fe}")
        elif choice == "7":
            participants = PList()


            available_participants = db.retrieve_all_participants()

            for participant in available_participants:
                participants.add_participant(Participant(*participant))

            participants.list_participants()

        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

    close_connection(db.conn)
