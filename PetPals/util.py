import pyodbc
from abc import ABC, abstractmethod
from datetime import datetime
import os
import dao
import exception
import entity

class Database:
    def __init__(self):
        self.conn = dao.connect_to_sql_server()

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
            raise exception.DatabaseOperationException("Failed to register participant.")

    def retrieve_all_participants(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Participants")
            pets = cursor.fetchall()
            return pets
        except pyodbc.Error as ex:
                    print(f"Error: {ex}")
                    return []





class CashDonation(entity.Donation):


    def record_donation(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Donations (DonationID,DonorName, DonationType, DonationAmount, DonationItem, DonationDate, ShelterID) VALUES (?,?, ?, ?, ?, ?, ?)",
                (self.donation_id, self.donor_name, self.donation_type, self.donation_amount, None, self.donation_date,
                 self.shelter_id))
            self.conn.commit()
            print(f"Cash donation of ${self.donation_amount} recorded on {self.donation_date} by {self.donor_name}")
        except pyodbc.Error as ex:
            print(f"Error recording cash donation: {ex}")


class ItemDonation(entity.Donation):
    def record_donation(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Donations (DonationID,DonorName, DonationType, DonationAmount, DonationItem, DonationDate, ShelterID) VALUES (?,?, ?, ?, ?, ?, ?)",
                (self.donation_id, self.donor_name, self.donation_type, self.donation_amount, self.donation_item,
                 self.donation_date, self.shelter_id))
            self.conn.commit()
            print(f"Item donation of {self.donation_item} worth ${self.donation_amount} recorded by {self.donor_name}")
        except pyodbc.Error as ex:
            print(f"Error recording item donation: {ex}")
