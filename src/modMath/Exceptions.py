class ModIntException(Exception):
    pass

class InvalidModError(ModIntException):
    pass

class InvalidModOperationError(ModIntException):
    pass

class InvalidTypeOperationError(ModIntException):
    pass

class InvalidInverseError(ModIntException):
    pass