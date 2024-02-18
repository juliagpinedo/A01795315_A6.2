"""
Customers Test

This program handles the Test Cases that will
be used to test the functionality of the
following functions:

- create_customer()
- delete_customer()
- display_customer_information()
- modify_customer_information()

It includes Test Cases with happy path,
negative path and edge cases

Author:
    Julia Gabriela Pinedo (A01795315)
"""

import unittest
from customers import Customers


class CustomersTest(unittest.TestCase):
    """
    Class to handle the Customers Test Cases
    """
    def setUp(self):
        """
        Setup method

        Returns:
            None
        """
        self.customers_obj = Customers()

    # PART 1: This part of the Test Cases include the Happy Path
    # scenarios, where all the values that are input are valid.

    def test_create_customer_happy_path(self):
        self.customers_obj.create_customer('1234',
                                           'Juan Lopez',
                                           'juanlopez@gmail.com',
                                           '2348760981')
        # Verifies customer exists
        self.assertIn('1234', self.customers_obj.customers)

    def test_display_customer_information_happy_path(self):
        self.customers_obj.create_customer('2345',
                                           'Karen Cat',
                                           'kcat@kittens.com',
                                           '6193459872')
        self.customers_obj.display_customer_information('2345')
        self.assertEqual(len(self.customers_obj.customers), 1)

    def test_modify_customer_information_happy_path(self):
        self.customers_obj.create_customer('1789',
                                           'Juan Peres',
                                           'juan@hotmial.com',
                                           '6645463789')
        self.customers_obj.modify_customer_information('1789',
                                                       'Juan Perez',
                                                       'juan@hotmail.com',
                                                       '6645463788')
        # Verifies that the modified customer information matches the expected values
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Juan Perez' and
                    customer_info['email'] == 'juan@hotmail.com' and
                    customer_info['phone'] == '6645463788'):
                modified_customer_found = True
                break
        self.assertTrue(modified_customer_found)

    def test_delete_customer_happy_path(self):
        # Creates a customer
        self.customers_obj.create_customer('4567',
                                           'Miley Cyrus',
                                           'mileycyrus@gmail.com',
                                           '6193427659')
        # Verifies customer exists before removing it
        self.assertIn('4567', self.customers_obj.customers)
        # Removes the customer
        self.customers_obj.delete_customer('4567')
        # Verifies customer no longer exists after removing it
        self.assertNotIn('4567', self.customers_obj.customers)

    # PART 2: This part of the Test Cases include the negative path
    # and edge case scenarios, where all the values are invalid or
    # some are missing/None.

    def test_create_customer_neg_path_1(self):
        # Path 1: Invalid name
        self.customers_obj.create_customer('4002',
                                           'Julia Pined0',
                                           'A01795315@tec.mx',
                                           '6643741600')
        # Verifies customer does not exist
        self.assertNotIn('4002', self.customers_obj.customers)

    def test_create_customer_neg_path_2(self):
        # Path 2: Invalid e-mail
        self.customers_obj.create_customer('4002',
                                           'Julia Pinedo',
                                           'A01795315@tec.!$0mx',
                                           '6643741600')
        # Verifies customer does not exist
        self.assertNotIn('4002', self.customers_obj.customers)

    def test_create_customer_neg_path_3(self):
        # Path 3: Invalid phone number
        self.customers_obj.create_customer('4002',
                                           'Julia Pinedo',
                                           'A01795315@tec.mx',
                                           '660')
        # Verifies customer does not exist
        self.assertNotIn('4002', self.customers_obj.customers)

    def test_create_customer_neg_path_4(self):
        # Path 4: Invalid ID
        self.customers_obj.create_customer('400',
                                           'Julia Pinedo',
                                           'A01795315@tec.mx',
                                           '6643741600')
        # Verifies customer does not exist
        self.assertNotIn('400', self.customers_obj.customers)

    def test_create_customer_neg_path_5(self):
        # Path 5: ID already exists
        self.customers_obj.create_customer('4000',
                                           'Julia Pinedo',
                                           'A01795315@tec.mx',
                                           '6643741600')
        self.customers_obj.create_customer('4000',
                                           'Jose Flores',
                                           'jflores@gmail.com',
                                           '6645411283')
        # Verifies customer doesn't exist with the duplicated information
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Jose Flores' and
                    customer_info['email'] == 'jflores@gmail.com' and
                    customer_info['phone'] == '6645411283'):
                modified_customer_found = True
                break
        self.assertFalse(modified_customer_found)

    def test_create_customer_neg_path_6(self):
        # Path 6: Empty Customer ID
        self.customers_obj.create_customer('',
                                           'Julia Pinedo',
                                           'A01795315@tec.mx',
                                           '6643741600')
        # Verifies customer does not exist
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_create_customer_neg_path_7(self):
        # Path 7: Empty Name
        self.customers_obj.create_customer('1604',
                                           '',
                                           'A01795315@tec.mx',
                                           '6643741600')
        # Verifies customer does not exist
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_create_customer_neg_path_8(self):
        # Path 8: Empty e-mail
        self.customers_obj.create_customer('1604',
                                           'Julia Pinedo',
                                           '',
                                           '6643741600')
        # Verifies customer does not exist
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_create_customer_neg_path_9(self):
        # Path 9: Empty phone number
        self.customers_obj.create_customer('1604',
                                           'Julia Pinedo',
                                           'A01795315@tec.mx',
                                           '')
        # Verifies customer does not exist
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_display_customer_information_neg_path_1(self):
        # Path 1: Invalid ID
        self.customers_obj.create_customer('0010',
                                           'Victoria Justice',
                                           'vj@nick.com',
                                           '6199991473')
        self.customers_obj.display_customer_information('001')
        self.assertEqual(len(self.customers_obj.customers), 1)

    def test_display_customer_information_neg_path_2(self):
        # Path 2: Customer ID does not exist
        self.customers_obj.display_customer_information('9854')
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_display_customer_information_neg_path_3(self):
        # Path 3: Customer ID was empty
        self.customers_obj.display_customer_information('')
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_modify_customer_information_neg_path_1(self):
        # Path 1: Customer ID does not exist
        self.customers_obj.modify_customer_information('2000',
                                                       'Adamari Lopez',
                                                       'adalopez@telemundo.us',
                                                       '9342671267')
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_modify_customer_information_neg_path_2(self):
        # Path 2: Invalid name
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information('6314',
                                                       'Travis Kelc3')
        # Verifies that the modified customer information matches the expected values
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Travis Kelce' and
                    customer_info['email'] == 'traviskc@chiefs.com' and
                    customer_info['phone'] == '6783215891'):
                modified_customer_found = True
                break
        self.assertTrue(modified_customer_found)

    def test_modify_customer_information_neg_path_3(self):
        # Path 3: Invalid e-mail
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information(customer_id='6314',
                                                       new_email='traviskc@ch--!$efz.c$$m')
        # Verifies that the modified customer information matches the expected values
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Travis Kelce' and
                    customer_info['email'] == 'traviskc@chiefs.com' and
                    customer_info['phone'] == '6783215891'):
                modified_customer_found = True
                break
        self.assertTrue(modified_customer_found)

    def test_modify_customer_information_neg_path_4(self):
        # Path 4: Invalid phone number
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information(customer_id='6314',
                                                       new_phone='1331')
        # Verifies that the modified customer information matches the expected values
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Travis Kelce' and
                    customer_info['email'] == 'traviskc@chiefs.com' and
                    customer_info['phone'] == '6783215891'):
                modified_customer_found = True
                break
        self.assertTrue(modified_customer_found)

    def test_modify_customer_information_neg_path_5(self):
        # Path 5: Changing just the name of the customer
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information('6314',
                                                       'Travis Swift')
        # Verifies that the modified customer information matches the expected values
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Travis Swift' and
                    customer_info['email'] == 'traviskc@chiefs.com' and
                    customer_info['phone'] == '6783215891'):
                modified_customer_found = True
                break
        self.assertTrue(modified_customer_found)

    def test_modify_customer_information_neg_path_6(self):
        # Path 6: Changing just the email of the customer
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information(customer_id='6314',
                                                       new_email='trav@tswift.com')
        # Verifies that the modified customer information matches the expected values
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Travis Kelce' and
                    customer_info['email'] == 'trav@tswift.com' and
                    customer_info['phone'] == '6783215891'):
                modified_customer_found = True
                break
        self.assertTrue(modified_customer_found)

    def test_modify_customer_information_neg_path_7(self):
        # Path 7: Changing just the phone number of the customer
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information(customer_id='6314',
                                                       new_phone='6191311214')
        # Verifies that the modified customer information matches the expected values
        modified_customer_found = False
        for customer_id, customer_info in self.customers_obj.customers.items():
            if (customer_info['name'] == 'Travis Kelce' and
                    customer_info['email'] == 'traviskc@chiefs.com' and
                    customer_info['phone'] == '6191311214'):
                modified_customer_found = True
                break
        self.assertTrue(modified_customer_found)

    def test_modify_customer_information_neg_path_8(self):
        # Path 8: Customer ID was empty
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information(customer_id='')
        self.assertEqual(len(self.customers_obj.customers), 1)

    def test_modify_customer_information_neg_path_9(self):
        # Path 9: Phone number was empty
        self.customers_obj.create_customer('6314',
                                           'Travis Kelce',
                                           'traviskc@chiefs.com',
                                           '6783215891')
        self.customers_obj.modify_customer_information(customer_id='6314',
                                                       new_phone='')
        self.assertEqual(len(self.customers_obj.customers), 1)

    def test_delete_customer_neg_path_1(self):
        # Path 1: Invalid Customer ID
        self.customers_obj.create_customer('4567',
                                           'Miley Cyrus',
                                           'mileycyrus@gmail.com',
                                           '6193427659')
        self.customers_obj.delete_customer('456')
        # Verifies customer exists because it wasn't removed
        self.assertIn('4567', self.customers_obj.customers)

    def test_delete_customer_neg_path_2(self):
        # Path 2: Customer ID does not exist
        self.customers_obj.delete_customer('1111')
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_delete_customer_neg_path_3(self):
        # Path 3: Customer ID already removed
        self.customers_obj.create_customer('4567',
                                           'Miley Cyrus',
                                           'mileycyrus@gmail.com',
                                           '6193427659')
        self.customers_obj.delete_customer('4567')
        self.customers_obj.delete_customer('4567')
        # Verifies customer no longer exists because it was already removed
        self.assertEqual(len(self.customers_obj.customers), 0)

    def test_delete_customer_neg_path_4(self):
        # Path 4: Customer ID was empty
        self.customers_obj.delete_customer('')
        self.assertEqual(len(self.customers_obj.customers), 0)


# This part of the code prints the results from the Unit Tests performed
if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(CustomersTest)

    # Run the tests and store the results
    test_result = unittest.TextTestRunner(stream=open('CustomersTestResults.txt', 'w'),
                                          verbosity=3).run(test_suite)
