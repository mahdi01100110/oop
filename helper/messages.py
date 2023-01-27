from enum import StrEnum


class PasswordErrors(StrEnum):
    PASSWORD_LENGTH_ERROR = "password must be at least 8 characters."
    PASSWORD_VALIDATION_ERROR = ' \
        password must have at least one integer,\
        password must have at least one character,\
        password must have at least one sign\
    '
