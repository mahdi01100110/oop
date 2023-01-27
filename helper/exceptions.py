from .messages import PasswordErrors


class WrongPasswordException(ValueError):
    pass

class PasswordLengthError(WrongPasswordException):
    '''When password length is too short'''
    def __str__(self):
        return PasswordErrors.PASSWORD_LENGTH_ERROR

class TypePasswordException(TypeError):
    pass

class WrongUsernameException(ValueError):
    pass

class TypeUsernameException(WrongUsernameException):
    pass

class UserDoesNotExist(WrongUsernameException):
    pass
