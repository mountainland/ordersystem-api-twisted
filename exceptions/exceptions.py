class UserNotFoundException(Exception):
    """Exception raised for errors in finding user.

    Attributes:
        username -- input username which caused the error
        message -- explanation of the error
    """

    def __init__(self, username, message="Username not found"):
        self.username = username
        self.message = message
        super().__init__(self.message)
