"""handler.py"""
class ReservationHandler(object):
    """reservation handler"""

    def __init__(self, **kwargs):
        self.sql_adapter = kwargs.get("sql_adapter")