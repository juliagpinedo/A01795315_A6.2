"""
Reservations

This program handles the operations related to the
reservations (creation and removal)

Author:
    Julia Gabriela Pinedo (A01795315)
"""
from hotels import Hotels
from customers import Customers


class Reservations:
    """
    Class to handle the reservations operations
    """
    def __init__(self, hotels: Hotels, customers: Customers):
        """
        Initialize the Reservations object

        Returns:
            None
        """
        self.hotels_instance = hotels
        self.customers_instance = customers
        self.reservations = []

    def create_customer_reservation(self, reservation_id, customer_id,
                                    hotel_name, room_number):
        """
        This method handles the reservation of a room from a Hotel

        Args:
            reservation_id (str): The ID of the reservation
            customer_id (str): The ID of the customer
            hotel_name (str): The name of the Hotel in which the
            reservation has been created
            room_number (str): The number of the reserved room

        Returns:
            None
        """
        if not self.validate_reservation_number(reservation_id):
            return

        for reservation in self.reservations:
            if reservation['reservation_id'] == reservation_id:
                print('\nError: Reservation already created')
                return

        if not self.validate_created_customer_id(customer_id):
            return

        if hotel_name.strip() == '':
            print('\nError: Hotel name cannot be empty')
            return

        if hotel_name not in self.hotels_instance.hotels:
            print(f'\nError: {hotel_name} does not exist')
            return

        if (room_number not in self.
                hotels_instance.hotels[hotel_name]['rooms']):
            print(f'\nError: Room {room_number} does not exist')
            return

        if (self.hotels_instance.hotels[hotel_name]['rooms']
                [room_number]['status'] == 'available'):
            # Reserve the room
            self.hotels_instance.reserve_room(hotel_name, room_number)
            # Store the reservation data
            reservation_data = {
                'reservation_id': reservation_id,
                'customer_id': customer_id,
                'hotel_name': hotel_name,
                'room_number': room_number
            }
            self.reservations.append(reservation_data)
            # Print the customer information
            self.customers_instance.\
                display_customer_information(customer_id)
            print(f'\nReservation successfully created. '
                  f'ID: {reservation_id}')
        else:
            print(f'\nError: Room {room_number} not available')

    @staticmethod
    def validate_reservation_number(reservation_id):
        """
        This method validates that the reservation number is valid

        Args:
            reservation_id (str): The ID of the reservation

        Returns:
            None
        """
        if reservation_id.strip() == '':
            print('\nError: Reservation ID cannot be empty')
            return False

        if (not isinstance(reservation_id, str)
                or len(reservation_id) != 6
                or not reservation_id.isdigit()):
            print('\nError: Invalid reservation ID')
            return False

        return True

    def validate_created_customer_id(self, customer_id):
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

        if (customer_id not in self.customers_instance.
                customers.keys()):
            print(f'\nError: ID {customer_id} does not exist')
            return False

        if (not isinstance(customer_id, str) or len(customer_id) != 4
                or not customer_id.isdigit()):
            print('\nError: Invalid Customer ID entered')
            return False

        return True

    def cancel_customer_reservation(self, reservation_id):
        """
        This method handles cancelling a reservation

        Args:
            reservation_id (str): The ID of the reservation

        Returns:
            None
        """
        if not self.validate_reservation_number(reservation_id):
            return

        for reservation in self.reservations:
            if reservation_id not in reservation['reservation_id']:
                print('\nError: Reservation does not exist')
                return

            if reservation['reservation_id'] == reservation_id:
                hotel_name = reservation['hotel_name']
                room_number = reservation['room_number']

                if (self.hotels_instance.hotels[hotel_name]['rooms']
                        [room_number]['status'] == 'reserved'):
                    self.hotels_instance.\
                     cancel_reservation(hotel_name, room_number)
                    print(f'\nReservation successfully removed. '
                          f'ID: {reservation_id}')
                    self.reservations.remove(reservation)
                    return
