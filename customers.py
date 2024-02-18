"""
Customers

This program handles the operations related to the
customers (creation, removal, information,
modification)

Author:
    Julia Gabriela Pinedo (A01795315)
"""
import re


class Customers:
    """
    Class to handle the customers operations
    """
    def __init__(self):
        """
        Initializes the Customers object

        Returns:
            None
        """
        self.customers = {}

    def create_customer(self, customer_id, name, email, phone):
        """
        This method handles the creation of a Hotel dictionary

        Args:
            customer_id (str): The ID of the customer to
            be created
            name (str): The name of the customer
            email (str): The email of the customer
            phone (str): The phone number of the customer

        Returns:
             None
        """
        if not self.validate_customer_id(customer_id):
            return

        if not self.validate_customer_name(name):
            return

        if not self.validate_customer_email(email):
            return

        if not self.validate_customer_phone(phone):
            return

        self.customers[customer_id] = {'name': name,
                                       'email': email,
                                       'phone': phone}
        print('\nCustomer created successfully')

    def validate_customer_id(self, customer_id):
        """
        This function validates that the customer ID entered exists

        Args:
            customer_id (str): The customer ID to be validated

        Returns:
            bool: True if the ID entered is valid, False otherwise
        """
        if customer_id.strip() == '':
            print('\nError: Customer ID cannot be empty')
            return False

        if customer_id in self.customers:
            print(f'\nError: {customer_id} already exists')
            return False

        if (not isinstance(customer_id, str) or len(customer_id) != 4
                or not customer_id.isdigit()):
            print('\nError: Invalid Customer ID entered')
            return False

        return True

    @staticmethod
    def validate_customer_name(customer_name):
        """
        This function validates the customer name entered

        Args:
            customer_name (str): The customer name to be validated

        Returns:
            bool: True if the name entered is valid, False
            otherwise
        """
        pattern = r"^[a-zA-Z\s\']+$"

        if customer_name.strip() == '':
            print('\nError: Customer name cannot be empty')
            return False

        if not re.fullmatch(pattern, customer_name):
            print('\nError: Customer name is invalid')
            return False

        return True

    @staticmethod
    def validate_customer_email(customer_email):
        """
        This function validates the customer email entered

        Args:
            customer_email (str): The customer email
            to be validated

        Returns:
            bool: True if the email entered is valid,
            False otherwise
        """
        pattern = (r"^[a-zA-Z0-9._%+-]+"
                   r"@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

        if customer_email.strip() == '':
            print('\nError: Customer email cannot be empty')
            return False

        if not re.fullmatch(pattern, customer_email):
            print('\nError: Customer email is invalid')
            return False

        return True

    @staticmethod
    def validate_customer_phone(customer_phone):
        """
        This function validates the customer phone number
        entered

        Args:
            customer_phone (str): The customer phone number
            to be validated

        Returns:
            bool: True if the phone number entered is valid,
            False otherwise
        """
        if customer_phone.strip() == '':
            print('\nError: Customer phone cannot be empty')
            return False

        if (not isinstance(customer_phone, str)
                or len(customer_phone) != 10
                or not customer_phone.isdigit()):
            print('\nError: Invalid Customer phone entered')
            return False

        return True

    def delete_customer(self, customer_id):
        """
        This method deletes a customer register (if it exists)

        Args:
            customer_id (str): The ID of the customer
             (already created)

        Returns:
            None
        """
        if customer_id.strip() == '':
            print('\nError: Customer ID cannot be empty')
            return

        if (not isinstance(customer_id, str) or len(customer_id) != 4
                or not customer_id.isdigit()):
            print('\nError: Invalid Customer ID entered')
            return

        if customer_id not in self.customers:
            print(f'\nError: ID {customer_id} does not exist')
            return

        del self.customers[customer_id]
        print(f'\nID: {customer_id} deleted successfully')

    def display_customer_information(self, customer_id):
        """
        This method displays the customer information (if it exists)

        Args:
            customer_id (str): The ID of the customer
            (already created)

        Returns:
            None
        """
        if customer_id.strip() == '':
            print('\nError: Customer ID cannot be empty')
            return

        if (not isinstance(customer_id, str) or len(customer_id) != 4
                or not customer_id.isdigit()):
            print('\nError: Invalid Customer ID entered')
            return

        if customer_id not in self.customers:
            print(f'\nError: ID {customer_id} does not exist')
            return

        customer_info = self.customers[customer_id]
        print('\nCustomer Information:')
        print(f'Customer ID: {customer_id}')
        print(f'Name: {customer_info["name"]}')
        print(f'E-mail: {customer_info["email"]}')
        print(f'Phone: {customer_info["phone"]}')

    def modify_customer_information(self, customer_id, new_name=None,
                                    new_email=None, new_phone=None):
        """
        This function updates the information of a customner

        Args:
            customer_id (str): The ID of the customer (already created)
            new_name (str): The new name of the customer (if applicable)
            new_email (str): The new email of the customer (if applicable)
            new_phone (str): The new phone of the customer (if applicable)

        Returns:
            None
        """
        if customer_id.strip() == '':
            print('\nError: Customer ID cannot be empty')
            return

        if (not isinstance(customer_id, str) or len(customer_id) != 4
                or not customer_id.isdigit()):
            print('\nError: Invalid Customer ID entered')
            return

        if customer_id not in self.customers:
            print(f'\nError: ID {customer_id} does not exist')
            return

        if new_name is not None:
            self.modify_customer_name(customer_id,
                                      new_name)

        if new_email is not None:
            self.modify_customer_email(customer_id,
                                       new_email)

        if new_phone is not None:
            self.modify_customer_phone(customer_id,
                                       new_phone)

    def modify_customer_name(self, customer_id, new_name):
        """
        This function modifies the name of a customer

        Args:
            customer_id (str): The ID of the customer
            new_name (str): The new name of the customer

        Returns:
            None
        """
        if not self.validate_customer_name(new_name):
            return

        if (customer_id in self.customers and
                self.customers[customer_id]['name'] == new_name):
            print('\nError: Name was not updated')
            return

        self.customers[customer_id]['name'] = new_name
        print(f'\nName updated to: {new_name}')

    def modify_customer_email(self, customer_id, new_email):
        """
        This function modifies the email of a customer

        Args:
            customer_id (str): The ID of the customer
            new_email (str): The new email of the customer

        Returns:
            None
        """
        if not self.validate_customer_email(new_email):
            return

        if (customer_id in self.customers and
                self.customers[customer_id]['email'] == new_email):
            print('\nError: E-mail was not updated')
            return

        self.customers[customer_id]['email'] = new_email
        print(f'\nE-mail updated to: {new_email}')

    def modify_customer_phone(self, customer_id, new_phone):
        """
        This function modifies the phone number of a customer

        Args:
            customer_id (str): The ID of the customer
            new_phone (str): The new phone number of the customer

        Returns:
            None
        """
        if not self.validate_customer_phone(new_phone):
            return

        if (customer_id in self.customers and
                self.customers[customer_id]['phone'] == new_phone):
            print('\nError: Phone number was not updated')
            return

        self.customers[customer_id]['phone'] = new_phone
        print(f'\nPhone number updated to: {new_phone}')
