from helper.exceptions import (
    PasswordLengthError,
    WrongUsernameException,
    TypePasswordException,
    TypeUsernameException
)

class BaseUser:

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeUsernameException("username must be `string`.")
        if not value[0].isalpha():
            raise WrongUsernameException("username must be start by character.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypePasswordException("password must be `string`.")
        if len(value) < 8:
            raise PasswordLengthError()
        self.__password = value

    def check_password(self, value):
        if self.password != value:
            raise ValueError("Password not match to confirm password.")

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.username}>'


class User(BaseUser):

    @classmethod
    def login(cls, username, password):
        is_authenticated = False
        user_pw = cls.read_password_from_file(username)
        username = cls.read_username_from_file(username)

        if password == user_pw:
            is_authenticated = True
        return is_authenticated

    def register(self, username, password):
        self.username = username
        self.password = password
        return self

    @staticmethod
    def read_password_from_file(username):
        with open('password.txt') as pw_file:
            user_password = pw_file.readline()
        return user_password

    def check_password(self, password):
        return True if self.password == password else False

    def check_username(self, username):
        return True if self.password == password else False