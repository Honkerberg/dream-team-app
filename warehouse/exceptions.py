### CUSTOM EXCEPTIONS - WAREHOUSE


class WrongPersonException(Exception):
    """Exception raised if wrong person is assigned to
    Employee/Customer.

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message="") -> None:
        self.message = message
        super().__init__(self.message)
