class UserNotFoundException(Exception):
    """Exception raised for errors in finding user.

    Attributes:
        username -- input username which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Username not found"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)