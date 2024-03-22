class OneBusAwayException(Exception):
    """Base exception for OneBusAway API errors."""

    pass


class APIKeyMissingError(OneBusAwayException):
    """Raised when the API key is missing."""

    pass


class APIKeyInvalidError(OneBusAwayException):
    """Raised when the API key is invalid or unauthorized."""

    pass


class BadRequestError(OneBusAwayException):
    """Raised when the server returns a 400 Bad Request response."""

    pass


class NotFoundError(OneBusAwayException):
    """Raised when the server returns a 404 Not Found response, indicating that the
    requested resource does not exist.
    """

    pass


class ServerError(OneBusAwayException):
    """Raised when the server returns a 5XX response, indicating a server-side error."""

    pass


class ResponseParseError(OneBusAwayException):
    """Raised when there is an error parsing the response from the API."""

    pass


class DataValidationError(OneBusAwayException):
    """Raised when there is a data validation error."""

    pass


class StopNotFoundError(OneBusAwayException):
    """Raised when a specified stop cannot be found."""

    pass


class TripNotFoundError(OneBusAwayException):
    """Raised when a specified trip cannot be found."""

    pass


class VehicleNotFoundError(OneBusAwayException):
    """Raised when a specified vehicle cannot be found."""

    pass


class ParameterError(OneBusAwayException):
    """Raised when there is an error with the provided parameters."""

    pass
