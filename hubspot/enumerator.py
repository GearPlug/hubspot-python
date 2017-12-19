from enum import Enum

class ErrorEnum(Enum):
    Unauthorized = 401
    Forbidden = 403
    TooManyRequests = 429
    Timeouts_1 = 502
    Timeouts_2 = 504
    NotFound = 404
    MethodNotAllowed = 405