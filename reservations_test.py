"""
Reservations Test

This program handles the Test Cases that will
be used to test the functionality of the
following functions:

- create_customer_reservation()
- cancel_customer_reservation()

It includes Test Cases with happy path,
negative path and edge cases

Author:
    Julia Gabriela Pinedo (A01795315)
"""

import unittest
from hotels import Hotels
from customers import Customers
from reservations import Reservations


class ReservationsTest(unittest.TestCase):
    """
    Class to handle the Reservations Test Cases
    """
    def setUp(self):
        """
        Setup method

        Returns:
            None
        """
        self.hotels_cls = Hotels()
        self.customers_cls = Customers()
        self.reservations_obj = Reservations(self.hotels_cls,
                                             self.customers_cls)

    # PART 1: This part of the Test Cases include the Happy Path
    # scenarios, where all the values that are input are valid.

    def test_create_customer_reservation_happy_path(self):
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('2386',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('100000',
                                                          '2386',
                                                          'Hotel California',
                                                          '102')
        # Verifies reservation exists
        reservation_found = False
        for reservation in self.reservations_obj.reservations:
            if reservation['reservation_id'] == '100000':
                reservation_found = True
                break
        self.assertTrue(reservation_found)

    def test_cancel_customer_reservation_happy_path(self):
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('4444',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('111111',
                                                          '4444',
                                                          'Hotel California',
                                                          '102')
        # Cancels the reservation
        self.reservations_obj.cancel_customer_reservation('111111')
        # Verifies reservation exists
        reservation_found = False
        for reservation in self.reservations_obj.reservations:
            if reservation['reservation_id'] == '111111':
                print(self.reservations_obj.reservations)
                reservation_found = True
                break
        self.assertFalse(reservation_found)

    # PART 2: This part of the Test Cases include the negative path
    # and edge case scenarios, where all the values are invalid or
    # some are missing/None.

    def test_create_customer_reservation_neg_path_1(self):
        # Path 1: Invalid reservation ID
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('2386',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('000',
                                                          '2386',
                                                          'Hotel California',
                                                          '102')
        self.assertEqual(len(self.reservations_obj.reservations), 0)

    def test_create_customer_reservation_neg_path_2(self):
        # Path 2: Customer ID not found
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('125429',
                                                          '1111',
                                                          'Hotel California',
                                                          '102')
        self.assertEqual(len(self.reservations_obj.reservations), 0)

    def test_create_customer_reservation_neg_path_3(self):
        # Path 3: Hotel name not found
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('2386',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('222222',
                                                          '2386',
                                                          'Hotel Quartz',
                                                          '101')
        self.assertEqual(len(self.reservations_obj.reservations), 0)

    def test_create_customer_reservation_neg_path_4(self):
        # Path 4: Room number doesn't exist
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('2386',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('222222',
                                                          '2386',
                                                          'Hotel California',
                                                          '104')
        self.assertEqual(len(self.reservations_obj.reservations), 0)

    def test_create_customer_reservation_neg_path_5(self):
        # Path 5: Reservation already created
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('2386',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        self.customers_cls.create_customer('3344',
                                           'Bill Kaulitz',
                                           'btk@tokio.com',
                                           '6193216783')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('222222',
                                                          '2386',
                                                          'Hotel California',
                                                          '101')
        self.reservations_obj.create_customer_reservation('333333',
                                                          '3344',
                                                          'Hotel California',
                                                          '101')
        self.assertEqual(len(self.reservations_obj.reservations), 1)

    def test_create_customer_reservation_neg_path_6(self):
        # Path 6: Room is not available
        # Create a Hotel
        rooms_info = {'483': {'status': 'reserved', 'type': 'double'}}
        self.hotels_cls.create_hotel('Hotel Tokio',
                                     'Berlin',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('1234',
                                           'Bill Kaulitz',
                                           'btk@tokio.com',
                                           '6193216783')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('111111',
                                                          '1234',
                                                          'Hotel Tokio',
                                                          '483')
        self.assertEqual(len(self.reservations_obj.reservations), 0)

    def test_create_customer_reservation_neg_path_7(self):
        # Path 7: Empty Hotel name
        # Create a Hotel
        rooms_info = {'101': {'status': 'available', 'type': 'single'}}
        self.hotels_cls.create_hotel('Hotel Wynn',
                                     'Las Vegas',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('1234',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('245792',
                                                          '1234',
                                                          '',
                                                          '101')
        self.assertEqual(len(self.reservations_obj.reservations), 0)

    def test_cancel_customer_reservation_neg_path_1(self):
        # Path 1: Invalid reservation ID
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('4444',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('111111',
                                                          '4444',
                                                          'Hotel California',
                                                          '102')
        # Cancels the reservation
        self.reservations_obj.cancel_customer_reservation('11')
        # Verifies reservation exists
        reservation_found = False
        for reservation in self.reservations_obj.reservations:
            if reservation['reservation_id'] == '111111':
                print(self.reservations_obj.reservations)
                reservation_found = True
                break
        self.assertTrue(reservation_found)

    def test_cancel_customer_reservation_neg_path_2(self):
        # Path 2: Reservation already canceled
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('4444',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('111111',
                                                          '4444',
                                                          'Hotel California',
                                                          '102')
        # Cancels the reservation
        self.reservations_obj.cancel_customer_reservation('111111')
        self.reservations_obj.cancel_customer_reservation('111111')
        # Verifies reservation exists
        reservation_found = False
        for reservation in self.reservations_obj.reservations:
            if reservation['reservation_id'] == '111111':
                print(self.reservations_obj.reservations)
                reservation_found = True
                break
        self.assertFalse(reservation_found)

    def test_cancel_customer_reservation_neg_path_3(self):
        # Path 3: Reservation ID was not found
        self.reservations_obj.cancel_customer_reservation('111111')
        self.assertEqual(len(self.reservations_obj.reservations), 0)

    def test_cancel_customer_reservation_neg_path_4(self):
        # Path 4: Empty reservation ID
        # Create a Hotel
        rooms_info = {
            '101': {'status': 'available', 'type': 'single'},
            '102': {'status': 'available', 'type': 'double'},
            '103': {'status': 'available', 'type': 'double'}
        }
        self.hotels_cls.create_hotel('Hotel California',
                                     'Tijuana',
                                     rooms_info)
        # Create a Customer
        self.customers_cls.create_customer('4444',
                                           'Jose Lopez',
                                           'jlopez@gmail.com',
                                           '6643127401')
        # Create a Reservation for the Customer
        self.reservations_obj.create_customer_reservation('111111',
                                                          '4444',
                                                          'Hotel California',
                                                          '102')
        # Cancels the reservation
        self.reservations_obj.cancel_customer_reservation('')
        # Verifies reservation exists
        reservation_found = False
        for reservation in self.reservations_obj.reservations:
            if reservation['reservation_id'] == '111111':
                print(self.reservations_obj.reservations)
                reservation_found = True
                break
        self.assertTrue(reservation_found)


# This part of the code prints the results from the Unit Tests performed
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReservationsTest)

    # Run the tests and store the results
    test_result = unittest.TextTestRunner(stream=open('ReservationsTestResults.txt', 'w'),
                                          verbosity=3).run(test_suite)
