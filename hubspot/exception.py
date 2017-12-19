class BaseError(Exception):
    pass

class Unauthorized(BaseError):
    pass

class Forbidden(BaseError):
    pass

class TooManyRequests(BaseError):
    pass

class Timeouts_1(BaseError):
    pass

class Timeouts_2(BaseError):
    pass

class UnexpectedError(BaseError):
    pass

class NotFound(BaseError):
    pass

class MethodNotAllowed(BaseError):
    pass

class ModuleNotFound(BaseError):
    pass