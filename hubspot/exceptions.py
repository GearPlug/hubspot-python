class BaseError(Exception):
    pass


class UnauthorizedError(BaseError):
    pass


class ForbiddenError(BaseError):
    pass


class TooManyRequestsError(BaseError):
    pass


class TimeoutError(BaseError):
    pass


class UnexpectedError(BaseError):
    pass


class NotFoundError(BaseError):
    pass


class MethodNotAllowedError(BaseError):
    pass


class ModuleNotFoundError(BaseError):
    pass
