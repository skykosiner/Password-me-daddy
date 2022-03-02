from dataclasses import dataclass
import json

@dataclass
class UserModel:
    username: str
    password: str

    def findByUsername(self):
        jsonObj = json.load(open('users.json', 'rb'))

        if jsonObj['username'] == self.username and jsonObj['password'] == self.password:
            return True
        else:
            return False
