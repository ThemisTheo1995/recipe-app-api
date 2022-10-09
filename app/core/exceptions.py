"""Exceptions for core."""


class CustomError(Exception):
    """Custom exception class."""
    pass


class UserModelEmailRequiredError(ValueError):
    """Raised when email is empty during registration."""

    def __init__(self, email, message="Email must not be an empty value."):
        self.email = email
        self.message = message
        super().__init__(self.message)
