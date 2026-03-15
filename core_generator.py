import random
import string

class EmailPasswordGenerator:
    def __init__(self, domain='gmail.com'):
        self.domain = domain

    def generate_email(self, username):
        return f'{username}@{self.domain}'

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(length))

    def generate_credentials(self, username):
        email = self.generate_email(username)
        password = self.generate_password()
        return email, password
