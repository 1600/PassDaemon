import bcrypt
 
 
class UserAccount:
 
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self._password = password
 
        @property
        def password(self):
            raise AttributeError('Password is not readable.')
 
        @password.setter
        def set_password(self, password):
            """Sets the user's password and hashes it"""
            salt = bcrypt.gensalt(16)
            hashed_password = bcrypt.hashpw(self.password.encode('utf8'), salt)
            return hashed_password.decode('utf8')
