from enum import Enum


class ErrorEnum(Enum):
    Unauthorized = 401
    Forbidden = 403
    TooManyRequests = 429
    Timeout1 = 502
    Timeout2 = 504
    NotFound = 404
    MethodNotAllowed = 405
