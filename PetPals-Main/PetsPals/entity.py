
from abc import ABC, abstractmethod

import PetsPals.exception

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
            # Implement adoption process
            print(f"Adoption process handled for pet {self._name}")
        except Exception as e:
            raise PetsPals.exception.AdoptionException(f"Error handling adoption: {e}")

    def __str__(self):
        try:
            return f"{self.name}, {self.age}, {self.breed}, {self.pet_type}, {self.available_for_adoption}, {self.shelter_name}, {self.owner_id}, {self.shelter_id}"
        except AttributeError:
            raise PetsPals.exception.NullReferenceException("Pet information is missing.")


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
                except PetsPals.exception.NullReferenceException as nre:
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
                except PetsPals.exception.NullReferenceException as nre:
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
                except PetsPals.exception.NullReferenceException as nre:
                    print(f"Error: {nre}")
                    continue
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