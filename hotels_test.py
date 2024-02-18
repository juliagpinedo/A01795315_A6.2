"""
Hotels Test

This program handles the Test Cases that will
be used to test the functionality of the
following functions:

- create_hotel()
- delete_hotel()
- display_hotel_information()
- modify_hotel_information()
- reserve_room()
- cancel_reservation()

It includes Test Cases with happy path,
negative path and edge cases

Author:
    Julia Gabriela Pinedo (A01795315)
"""

import unittest
from hotels import Hotels


class HotelsTest(unittest.TestCase):
    """
    Class to handle the Customers Test Cases
    """
    def setUp(self):
        """
        Setup method

        Returns:
            None
        """
        self.hotels_obj = Hotels()

    # PART 1: This part of the Test Cases include the Happy Path
    # scenarios, where all the values that are input are valid.

    def test_create_hotel_happy_path(self):
        # Dictionary with the rooms information
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Camino Real',
                                     'Tijuana',
                                     rooms_info)
        # Verifies hotel exists
        self.assertIn('Hotel Camino Real', self.hotels_obj.hotels)

    def test_delete_hotel_happy_path(self):
        # Dictionary with the rooms information
        rooms_info = {
            '201': {'status': 'available', 'type': 'single'},
            '202': {'status': 'available', 'type': 'double'},
            '203': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'San Diego',
                                     rooms_info)
        # Verifies hotel exists before removing it
        self.assertIn('Hotel Hilton', self.hotels_obj.hotels)
        self.hotels_obj.delete_hotel('Hotel Hilton')
        # Verifies hotel no longer exists after removing it
        self.assertNotIn('Hotel Camino Real', self.hotels_obj.hotels)

    def test_display_hotel_information_happy_path(self):
        # Dictionary with the rooms information
        rooms_info = {
            '201': {'status': 'available', 'type': 'single'},
            '202': {'status': 'available', 'type': 'double'},
            '203': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'San Diego',
                                     rooms_info)
        self.hotels_obj.display_hotel_information('Hotel Hilton')
        self.assertEqual(len(self.hotels_obj.hotels), 1)

    def test_modify_hotel_information_happy_path(self):
        # Dictionary with the rooms information
        rooms_info = {'201': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hoteel Hiltooon',
                                     'Saaan Diegoo',
                                     rooms_info)
        # Dictionary with the new rooms information
        new_rooms_info = {'201': {'status': 'reserved', 'type': 'double'}}
        self.hotels_obj.modify_hotel_information('Hoteel Hiltooon',
                                                 'Hotel Hilton',
                                                 'San Diego',
                                                 new_rooms_info)
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Hilton' and
                    hotel_info['location'] == 'San Diego' and
                    hotel_info['rooms'] == new_rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_reserve_room_happy_path(self):
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.reserve_room('Hotel Jackson', '101')
        reserved_room = {'101': {'status': 'reserved', 'type': 'single'}}
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == reserved_room:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_cancel_reservation_happy_path(self):
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'reserved', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.cancel_reservation('Hotel Jackson', '101')
        available_room = {'101': {'status': 'available', 'type': 'single'}}
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == available_room:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    # PART 2: This part of the Test Cases include the negative path
    # and edge case scenarios, where all the values are invalid or
    # some are missing/None.

    def test_create_hotel_neg_path_1(self):
        # Path 1: Empty name
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('',
                                     'Tijuana',
                                     rooms_info)
        # Verifies hotel doesn't exist
        self.assertEqual(len(self.hotels_obj.hotels), 0)

    def test_create_hotel_neg_path_2(self):
        # Path 2: Invalid location
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'T!!jU00n4',
                                     rooms_info)
        # Verifies hotel doesn't exist
        self.assertNotIn('Hotel Ticuan', self.hotels_obj.hotels)

    def test_create_hotel_neg_path_3(self):
        # Path 3: Invalid hotel room number
        # Dictionary with the rooms information
        rooms_info = {'5000': {'status': 'available', 'type': 'single'},
                      '100': {'status': 'reserved', 'type': 'double'}}
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'Tijuana',
                                     rooms_info)
        # Verifies that the modified hotel information matches the expected values
        accepted_info = {'100': {'status': 'reserved', 'type': 'double'}}
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Ticuan' and
                    hotel_info['location'] == 'Tijuana' and
                    hotel_info['rooms'] == accepted_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_create_hotel_neg_path_4(self):
        # Path 4: Invalid hotel room number
        # Dictionary with the rooms information
        rooms_info = {'100': {'status': 'disponible', 'type': 'single'},
                      '101': {'status': 'reserved', 'type': 'double'}}
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'Tijuana',
                                     rooms_info)
        # Verifies that the modified hotel information matches the expected values
        accepted_info = {'101': {'status': 'reserved', 'type': 'double'}}
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Ticuan' and
                    hotel_info['location'] == 'Tijuana' and
                    hotel_info['rooms'] == accepted_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_create_hotel_neg_path_5(self):
        # Path 5: Invalid hotel room type
        # Dictionary with the rooms information
        rooms_info = {'100': {'status': 'available', 'type': 'triple'},
                      '101': {'status': 'reserved', 'type': 'double'}}
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'Tijuana',
                                     rooms_info)
        # Verifies that the modified hotel information matches the expected values
        accepted_info = {'101': {'status': 'reserved', 'type': 'double'}}
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Ticuan' and
                    hotel_info['location'] == 'Tijuana' and
                    hotel_info['rooms'] == accepted_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_create_hotel_neg_path_6(self):
        # Path 6: Empty room status
        # Dictionary with the rooms information
        rooms_info = {'100': {'status': '', 'type': 'single'},
                      '101': {'status': 'reserved', 'type': 'double'}}
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'Tijuana',
                                     rooms_info)
        # Verifies that the modified hotel information matches the expected values
        accepted_info = {'101': {'status': 'reserved', 'type': 'double'}}
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Ticuan' and
                    hotel_info['location'] == 'Tijuana' and
                    hotel_info['rooms'] == accepted_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_create_hotel_neg_path_7(self):
        # Path 7: Empty type
        # Dictionary with the rooms information
        rooms_info = {'100': {'status': 'available', 'type': ''},
                      '101': {'status': 'reserved', 'type': 'double'}}
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'Tijuana',
                                     rooms_info)
        # Verifies that the modified hotel information matches the expected values
        accepted_info = {'101': {'status': 'reserved', 'type': 'double'}}
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Ticuan' and
                    hotel_info['location'] == 'Tijuana' and
                    hotel_info['rooms'] == accepted_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_create_hotel_neg_path_8(self):
        # Path 8: Hotel already created
        # Dictionary with the rooms information
        rooms_info = {'100': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'Tijuana',
                                     rooms_info)
        self.hotels_obj.create_hotel('Hotel Ticuan',
                                     'Tijuana',
                                     rooms_info)
        self.assertEqual(len(self.hotels_obj.hotels), 1)

    def test_delete_hotel_neg_path_1(self):
        # Path 1: Invalid Hotel name was provided
        # Dictionary with the rooms information
        rooms_info = {'201': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'San Diego',
                                     rooms_info)
        self.hotels_obj.delete_hotel('Hotel Hiltons')
        # Verifies hotel exists because it wasn't removed
        self.assertIn('Hotel Hilton', self.hotels_obj.hotels)

    def test_delete_hotel_neg_path_2(self):
        # Path 2: Hotel name provided was empty
        self.hotels_obj.delete_hotel('')
        self.assertEqual(len(self.hotels_obj.hotels), 0)

    def test_delete_hotel_neg_path_3(self):
        # Path 3: Hotel was already removed
        # Dictionary with the rooms information
        rooms_info = {'201': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'San Diego',
                                     rooms_info)
        self.hotels_obj.delete_hotel('Hotel Hilton')
        self.hotels_obj.delete_hotel('Hotel Hilton')
        # Verifies hotel no longer exists because it was already removed
        self.assertEqual(len(self.hotels_obj.hotels), 0)

    def test_delete_hotel_neg_path_4(self):
        # Path 4: Hotel name does not exist
        self.hotels_obj.delete_hotel('Hotel Paris')
        # Verifies hotel no longer exists because it was already removed
        self.assertEqual(len(self.hotels_obj.hotels), 0)

    def test_display_hotel_information_neg_path_1(self):
        # Path 1: Empty Hotel name
        # Dictionary with the rooms information
        rooms_info = {
            '201': {'status': 'available', 'type': 'single'},
            '202': {'status': 'available', 'type': 'double'},
            '203': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'San Diego',
                                     rooms_info)
        self.hotels_obj.display_hotel_information('')
        self.assertEqual(len(self.hotels_obj.hotels), 1)

    def test_display_hotel_information_neg_path_2(self):
        # Path 2: Hotel doesn't exist
        # Dictionary with the rooms information
        self.hotels_obj.display_hotel_information('Hotel Xcaret')
        self.assertEqual(len(self.hotels_obj.hotels), 0)

    def test_display_hotel_information_neg_path_3(self):
        # Path 3: Invalid Hotel name
        # Dictionary with the rooms information
        self.hotels_obj.display_hotel_information('H00$$$$terl Sc_---')
        self.assertEqual(len(self.hotels_obj.hotels), 0)

    def test_modify_hotel_information_neg_path_1(self):
        # Path 1: Invalid Hotel name
        # Dictionary with the rooms information
        rooms_info = {
            '201': {'status': 'available', 'type': 'single'},
            '202': {'status': 'available', 'type': 'double'},
            '203': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Trump',
                                     'Las Vega',
                                     rooms_info)
        # Dictionary with the new rooms information
        new_rooms_info = {'201': {'status': 'reserved', 'type': 'double'}}
        self.hotels_obj.modify_hotel_information('',
                                                 'Hotel International',
                                                 'Las Vegas',
                                                 new_rooms_info)
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Trump' and
                    hotel_info['location'] == 'Las Vega' and
                    hotel_info['rooms'] == rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_2(self):
        # Path 2: Invalid location
        # Dictionary with the rooms information
        rooms_info = {
            '201': {'status': 'available', 'type': 'single'},
            '202': {'status': 'available', 'type': 'double'},
            '203': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Trump',
                                     'Las Vega',
                                     rooms_info)
        self.hotels_obj.modify_hotel_information('Hotel Trump',
                                                 'Hotel International',
                                                 'La$$ Veg22s')
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel International' and
                    hotel_info['location'] == 'Las Vega' and
                    hotel_info['rooms'] == rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_3(self):
        # Path 3: Invalid status
        # Dictionary with the rooms information
        rooms_info = {
            '201': {'status': 'available', 'type': 'single'},
            '202': {'status': 'available', 'type': 'double'},
            '203': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Trump',
                                     'Las Vega',
                                     rooms_info)
        # Dictionary with the new rooms information
        new_rooms_info = {'201': {'status': 'reservado'}}
        self.hotels_obj.modify_hotel_information('Hotel Trump',
                                                 'Hotel International',
                                                 'Las Vegas',
                                                 new_rooms_info)
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel International' and
                    hotel_info['location'] == 'Las Vegas' and
                    hotel_info['rooms'] == rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_4(self):
        # Path 4: Invalid room type
        # Dictionary with the rooms information
        rooms_info = {
            '201': {'status': 'available', 'type': 'single'},
            '202': {'status': 'available', 'type': 'double'},
            '203': {'status': 'available', 'type': 'double'}
        }
        self.hotels_obj.create_hotel('Hotel Trump',
                                     'Las Vega',
                                     rooms_info)
        # Dictionary with the new rooms information
        new_rooms_info = {'201': {'type': 'triple'}}
        self.hotels_obj.modify_hotel_information('Hotel Trump',
                                                 'Hotel International',
                                                 'Las Vegas',
                                                 new_rooms_info)
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel International' and
                    hotel_info['location'] == 'Las Vegas' and
                    hotel_info['rooms'] == rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_5(self):
        # Path 5: Edit Location without changing the Hotel name
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'Las Vegaz',
                                     rooms_info)
        self.hotels_obj.modify_hotel_information(hotel_name='Hotel Hilton',
                                                 new_location='Las Vegas')
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Hilton' and
                    hotel_info['location'] == 'Las Vegas' and
                    hotel_info['rooms'] == rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_6(self):
        # Path 6: Edit room status without changing type or location
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'Las Vegas',
                                     rooms_info)
        # Dictionary with the new rooms information
        new_rooms_info = {'101': {'status': 'reserved'}}
        self.hotels_obj.modify_hotel_information(hotel_name='Hotel Hilton',
                                                 new_room_info=new_rooms_info)
        # Expected rooms dict
        exp_info = {'101': {'status': 'reserved', 'type': 'single'}}
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Hilton' and
                    hotel_info['location'] == 'Las Vegas' and
                    hotel_info['rooms'] == exp_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_7(self):
        # Path 7: Edit room type without changing status or location
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'Las Vegas',
                                     rooms_info)
        # Dictionary with the new rooms information
        new_rooms_info = {'101': {'type': 'double'}}
        self.hotels_obj.modify_hotel_information(hotel_name='Hotel Hilton',
                                                 new_room_info=new_rooms_info)
        # Expected rooms dict
        exp_info = {'101': {'status': 'available', 'type': 'double'}}
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Hilton' and
                    hotel_info['location'] == 'Las Vegas' and
                    hotel_info['rooms'] == exp_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_8(self):
        # Path 8: Edit Hotel name with the same name
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'Las Vegas',
                                     rooms_info)
        self.hotels_obj.modify_hotel_information(hotel_name='Hotel Hilton',
                                                 new_hotel_name='Hotel Hilton')
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Hilton' and
                    hotel_info['location'] == 'Las Vegas' and
                    hotel_info['rooms'] == rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_modify_hotel_information_neg_path_9(self):
        # Path 9: Edit Hotel location with the same location
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Hilton',
                                     'Las Vegas',
                                     rooms_info)
        self.hotels_obj.modify_hotel_information(hotel_name='Hotel Hilton',
                                                 new_location='Las Vegas')
        # Verifies that the modified hotel information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if (hotel_name == 'Hotel Hilton' and
                    hotel_info['location'] == 'Las Vegas' and
                    hotel_info['rooms'] == rooms_info):
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_reserve_room_neg_path_1(self):
        # Path 1: Invalid hotel name provided
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.reserve_room('', '101')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_reserve_room_neg_path_2(self):
        # Path 2: Invalid room number provided
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.reserve_room('Hotel Jackson', '0000')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_reserve_room_neg_path_3(self):
        # Path 3: Hotel room already reserved
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'reserved', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.reserve_room('Hotel Jackson', '101')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_reserve_room_neg_path_4(self):
        # Path 4: Invalid room number
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.reserve_room('Hotel Jackson', '')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_cancel_reservation_neg_path_1(self):
        # Path 1: Invalid hotel name provided
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'reserved', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.cancel_reservation('', '101')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_cancel_reservation_neg_path_2(self):
        # Path 2: Invalid room number provided
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'reserved', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.cancel_reservation('Hotel Jackson', '0000')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_cancel_reservation_neg_path_3(self):
        # Path 3: Hotel room already available
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.cancel_reservation('Hotel Jackson', '101')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    def test_cancel_reservation_neg_path_4(self):
        # Path 4: Invalid room number
        # Dictionary with the rooms information
        rooms_info = {'101': {'status': 'reserved', 'type': 'single'}}
        self.hotels_obj.create_hotel('Hotel Jackson',
                                     'Los Angeles',
                                     rooms_info)
        self.hotels_obj.cancel_reservation('Hotel Jackson', '')
        # Verifies that the modified room information matches the expected values
        modified_hotel_found = False
        for hotel_name, hotel_info in self.hotels_obj.hotels.items():
            if hotel_info['rooms'] == rooms_info:
                modified_hotel_found = True
                break
        self.assertTrue(modified_hotel_found)

    # Additional


# This part of the code prints the results from the Unit Tests performed
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(HotelsTest)

    # Run the tests and store the results
    test_result = unittest.TextTestRunner(stream=open('HotelsTestResults.txt', 'w'),
                                          verbosity=3).run(test_suite)
