"""handler.py"""

import queries
from domain import Reservation


class ReservationHandler(object):
    """reservation handler"""

    def __init__(self, **kwargs):
        """consructor"""
        self.sql_adapter = kwargs.get("sql_adapter")

    def get_reservations(self):
        """get all resis"""
        reservations_data = self.sql_adapter.execute(queries.GET_RESERVATIONS)

        # map data to Reservation objects
        reservations = []
        for data in reservations_data:
            reservation = Reservation(
                reservation_date=data["reservation_date"],
                venue_name=data["venue_name"],
                venue_location=data["venue_location"],
                customer_name=data["customer_name"],
                seat_section=data["seat_section"],
                seat_row=data["seat_row"],
                seat_number=data["seat_number"],
                is_held=data["is_held"],
            )
            reservations.append(reservation.serialize())

        return reservations
