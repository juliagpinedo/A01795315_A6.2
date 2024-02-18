"""
Hotels

This program handles the operations related to the hotels
(creation, removal, information, reservation)

Author:
    Julia Gabriela Pinedo (A01795315)
"""
import re


class Hotels:
    """
    Class to handle the hotels operations
    """
    def __init__(self):
        """
        Initializes the Hotels object

        Returns:
            None
        """
        self.hotels = {}

    def create_hotel(self, hotel_name, location, rooms_info):
        """
        This method handles the creation of a Hotel dictionary

        Args:
            hotel_name (str): The name of the Hotel to be created
            location (str): The location of the Hotel
            rooms_info (dict): A dictionary containing the room
            numbers as keys and dictionaries containing room details
            (status, type) as values

        Returns:
             None
        """
        if not self.validate_hotel_name(hotel_name):
            return

        if not self.validate_hotel_location(location):
            return

        # Creates the "Hotel" dictionary
        self.hotels[hotel_name] = {'location': location, 'rooms': {}}
        print(f'\n{hotel_name} created successfully')

        for room_number, room_details in rooms_info.items():
            if (not isinstance(room_number, str) or len(room_number) != 3
                    or not room_number.isdigit()):
                print('\nError: Invalid room number')
                continue

            status = room_details.get('status')
            if status not in ['reserved', 'available']:
                print(f'\nError: Invalid room status for room {room_number}')
                continue

            room_type = room_details.get('type')
            if room_type not in ['single', 'double']:
                print(f'\nError: Invalid room type for room {room_number}')
                continue

            # Creates the "rooms_info" dictionary
            self.create_hotel_room(hotel_name, room_number, status, room_type)

    def create_hotel_room(self, hotel_name, room_number, status, room_type):
        """
        This method creates a hotel room dictionary for a given hotel

        Args:
            hotel_name (str): The name of the Hotel (already created)
            room_number (str): The number of the room(s) of the Hotel
            status (str): The status of the room(s), 'reserved' or 'available'
            room_type (str): The type of room(s), 'single' or 'double'

        Returns:
            None
        """
        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return

        if hotel_name not in self.hotels:
            print(f'\nError: {hotel_name} does not exist')
            return

        if room_number in self.hotels[hotel_name]['rooms']:
            print(f'\nError: {room_number} already exists')
            return

        self.hotels[hotel_name]['rooms'][room_number] = \
            {'status': status, 'type': room_type}
        print(f'\nRoom {room_number} added successfully to {hotel_name}')

    def delete_hotel(self, hotel_name):
        """
        This method deletes a Hotel register (if it exists)

        Args:
            hotel_name (str): The name of the Hotel (already created)

        Returns:
            None
        """
        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return

        if hotel_name not in self.hotels:
            print(f'\nError: {hotel_name} does not exist')
            return

        del self.hotels[hotel_name]
        print(f'\n{hotel_name} deleted successfully')

    def display_hotel_information(self, hotel_name):
        """
        This method displays the information of a Hotel (if it exists)

        Args:
            hotel_name (str): The name of the Hotel (already created)

        Returns:
            None
        """
        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return

        if hotel_name not in self.hotels:
            print(f'\nError: {hotel_name} does not exist')
            return

        print(f'\n{hotel_name} Information:')
        print(f'Location: {self.hotels[hotel_name]["location"]}')
        print('Rooms:')
        for room, room_info in self.hotels[hotel_name]["rooms"].items():
            print(f'    Room No.: {room}')
            for key, value in room_info.items():
                print(f'      {key.capitalize()}: {value}')

    def modify_hotel_information(self, hotel_name, new_hotel_name=None,
                                 new_location=None, new_room_info=None):
        """
        This function modifies the information of a Hotel: its name,
        location and rooms information

        Args:
            hotel_name (str): The name of the existing Hotel (already created)
            new_hotel_name (str): The name to change (if applicable)
            new_location (str): The location to change (if applicable)
            new_room_info (dict): The rooms information to change
            (if applicable)

        Returns:
            None
        """
        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return

        if hotel_name not in self.hotels:
            print(f'\nError: {hotel_name} does not exist')
            return

        if new_hotel_name is not None:
            self.modify_hotel_name(hotel_name, new_hotel_name)

        if new_location is not None:
            self.modify_hotel_location(hotel_name, new_hotel_name,
                                       new_location)

        if new_room_info is not None:
            self.modify_hotel_rooms(hotel_name, new_hotel_name,
                                    new_room_info)

    def validate_hotel_name(self, hotel_name):
        """
        This function validates that the Hotel name entered exists

        Args:
            hotel_name (str): The Hotel name to be validated

        Returns:
            bool: True if the Hotel name entered is valid, False otherwise
        """
        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return False

        if hotel_name in self.hotels:
            print(f'\nError: {hotel_name} already exists')
            return False

        return True

    @staticmethod
    def validate_hotel_location(hotel_location):
        """
        This function validates the Hotel location entered

        Args:
            hotel_location (str): The Hotel location to be validated

        Returns:
            bool: True if the Hotel location entered is valid, False
            otherwise
        """
        pattern = r"^[a-zA-Z\s\']+$"

        if hotel_location.strip() == '':
            print('\nError: Location name cannot be empty')
            return False

        if not re.fullmatch(pattern, hotel_location):
            print('\nError: Location name is invalid')
            return False

        return True

    @staticmethod
    def validate_room_information(room_number, room_details):
        """
        This function validates the Room information entered as a dictionary

        Args:
            room_number (str): The Room number to edit its details
            room_details (dict): The Room details to be edited

        Returns:
            bool: True if the Room information entered is valid, False
            otherwise
            status: The status of the Room
            room_type: The type of the Room
        """
        if (not isinstance(room_number, str) or len(room_number) != 3
                or not room_number.isdigit()):
            print('\nError: Invalid room number')
            return False, None, None

        status = room_details.get('status')
        if status is not None and status not in ['reserved', 'available']:
            print(f'\nError: Invalid room status for room {room_number}')
            return False, None, None

        room_type = room_details.get('type')
        if room_type is not None and room_type not in ['single', 'double']:
            print(f'\nError: Invalid room type for room {room_number}')
            return False, None, None

        return True, status, room_type

    def modify_hotel_name(self, hotel_name, new_hotel_name):
        """
        This function modifies the Hotel name to a different one

        Args:
            hotel_name (str): The original name of the Hotel
            new_hotel_name (str): The new name of the Hotel

        Returns:
            None
        """
        if not self.validate_hotel_name(new_hotel_name):
            return

        self.hotels[new_hotel_name] = self.hotels.pop(hotel_name)
        print(f'\n{hotel_name} successfully changed to {new_hotel_name}')

    def modify_hotel_location(self, hotel_name, new_hotel_name,
                              new_location):
        """
        This function modifies the location of a Hotel

        Args:
            hotel_name (str): The original Hotel name
            new_hotel_name (str): The new name of the Hotel (if applicable)
            new_location (str): The new location of the Hotel (if applicable)

        Returns:
            None
        """
        if not self.validate_hotel_location(new_location):
            return

        if (hotel_name in self.hotels and
            self.hotels[hotel_name]['location'] == new_location) or \
                (new_hotel_name is not None and new_hotel_name in
                 self.hotels and self.hotels[new_hotel_name]['location'] ==
                 new_location):
            print('\nError: Location was not updated')
            return

        if new_hotel_name is None:
            self.hotels[hotel_name]['location'] = new_location
        else:
            self.hotels[new_hotel_name]['location'] = new_location
        print(f'\nLocation updated to: {new_location}')

    def modify_hotel_rooms(self, hotel_name, new_hotel_name,
                           new_room_info):
        """
        This function updates the information from a Hotel room

        Args:
            hotel_name (str): The original Hotel name
            new_hotel_name (str): The new name of the Hotel (if applicable)
            new_room_info (dict): A dictionary containing the
            new room information (if applicable)

        Returns:
            None
        """
        for room_number, room_details in new_room_info.items():
            # Validates the "new_room_info" dictionary provided
            is_valid, status, room_type = \
                self.validate_room_information(room_number, room_details)

            if not is_valid:
                continue

            if new_hotel_name is None:
                if room_number in self.hotels[hotel_name]['rooms']:
                    if status is not None:
                        self.\
                            hotels[hotel_name]['rooms'][room_number]['status']\
                            = status
                    if room_type is not None:
                        self.\
                            hotels[hotel_name]['rooms'][room_number]['type']\
                            = room_type
                else:
                    print('\nError: Room does not exist')
            else:
                if room_number in self.hotels[new_hotel_name]['rooms']:
                    if status is not None:
                        (self.hotels[new_hotel_name]
                            ['rooms'][room_number]['status']) = status
                    if room_type is not None:
                        (self.hotels[new_hotel_name]
                            ['rooms'][room_number]['type']) = room_type
                else:
                    print('\nError: Room does not exist')
            print('\nRoom information updated successfully')

    def reserve_room(self, hotel_name, room_number):
        """
        This function reserves a room in the given Hotel

        Args:
            hotel_name (str): The Hotel name
            room_number (str): The room number that will be reserved

        Returns:
            None
        """
        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return

        if hotel_name not in self.hotels:
            print(f'\nError: {hotel_name} does not exist')
            return

        if (not isinstance(room_number, str) or len(room_number) != 3
                or not room_number.isdigit()):
            print('\nError: Invalid room number')
            return

        if room_number not in self.hotels[hotel_name]['rooms']:
            print(f'\nError: Room {room_number} does not exist')

        if (self.hotels[hotel_name]['rooms'][room_number]['status']
                == 'reserved'):
            print(f'\nError: Room {room_number} is not available')

        self.\
            hotels[hotel_name]['rooms'][room_number]['status'] \
            = 'reserved'
        print(f'\nRoom {room_number} reserved successfully')

    def cancel_reservation(self, hotel_name, room_number):
        """
        This function cancels the reservation of a room in the given Hotel

        Args:
            hotel_name (str): The Hotel name
            room_number (str): The room number that will be cancelled

        Returns:
            None
        """
        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return

        if hotel_name not in self.hotels:
            print(f'\nError: {hotel_name} does not exist')
            return

        if (not isinstance(room_number, str) or len(room_number) != 3
                or not room_number.isdigit()):
            print('\nError: Invalid room number')
            return

        if room_number not in self.hotels[hotel_name]['rooms']:
            print(f'\nError: Room {room_number} does not exist')

        if (self.hotels[hotel_name]['rooms'][room_number]['status']
                == 'available'):
            print(f'\nError: Room {room_number} is available')

        self. \
            hotels[hotel_name]['rooms'][room_number]['status'] \
            = 'available'
        print(f'\nRoom {room_number} cancelled successfully')
