class Reservation:
    def __init__(self, **kwargs):
        """constructor"""
        self.reservation_date = kwargs.get('reservation_date')
        self.venue_name = kwargs.get('venue_name')
        self.venue_location = kwargs.get('venue_location')
        self.customer_name = kwargs.get('customer_name')
        self.seat_section = kwargs.get('seat_section')
        self.seat_row = kwargs.get('seat_row')
        self.seat_number = kwargs.get('seat_number')
        self.is_held = kwargs.get('is_held')


    def serialize(self):
        """return dict (kv)"""
        return self.__dict__