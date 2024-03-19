import pyodbc
from abc import ABC, abstractmethod
from datetime import datetime
import os
import dao
import exception
import entity
import util


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
        raise exception.FileHandlingException("File not found.")
    except IOError:
        raise exception.FileHandlingException("Error reading file.")


if __name__ == "__main__":

    db = util.Database()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":

            shelter = entity.PetShelter()

            pets = db.get_available_pets()
            for pet in pets:
                shelter.add_pet(entity.Pet(*pet))

            shelter.list_available_pets()
        elif choice == "2":
            try:
                donation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                donation_id = input("Enter donation ID: ")
                donor_name = input("Enter donor name: ")
                donation_amount = float(input("Enter donation amount: "))
                cash_donation = util.CashDonation(donation_id, donor_name, "Cash", donation_amount, None, donation_date, 1)
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
                item_donation = util.ItemDonation(donation_id, donor_name, "Item", donation_amount, donation_item,
                                             donation_date, 1)
                item_donation.record_donation()
            except ValueError as ve:
                print(f"Error: {ve}")
        elif choice == "4":

            try:
                events = db.get_upcoming_events()
                event_manager = entity.AdoptionEventManager()
                for event in events:
                    event_manager.add_event(entity.AdoptionEvent(*event))
                event_manager.list_events()
            except exception.DatabaseOperationException as doe:
                print(f"Database Operation Error: {doe}")
        elif choice == "5":
            try:
                participant_id = input("Enter your ID : ")
                event_id = input("Enter event ID to register for: ")
                participant_name = input("Enter your name: ")
                participant_email = input("Enter your email: ")
                city = input("Enter event City: ")
                db.register_participant(participant_id, participant_name, participant_email, event_id, city)
            except exception.DatabaseOperationException as doe:
                print(f"Database Operation Error: {doe}")
        elif choice == "6":
            try:
                file_name = input("Enter the file name: ")
                file_path = os.path.join(os.getcwd(), file_name)
                data = read_data_from_file(file_path)
                print("Data read successfully:")
                print(data)
            except exception.FileHandlingException as fe:
                print(f"File Handling Error: {fe}")
        elif choice == "7":
            participants = entity.PList()


            available_participants = db.retrieve_all_participants()

            for participant in available_participants:
                participants.add_participant(entity.Participant(*participant))

            participants.list_participants()

        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

    dao.close_connection(db.conn)
