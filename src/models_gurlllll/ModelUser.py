from dataclasses import dataclass
import json

@dataclass
class UserModel:
    username: str
    password: str

    def findByUsername(self):
        # load the json file into jsonObj variable gurllll
        jsonObj = json.load(open('users.json', 'rb'))

        # Check if the username and password are correct or even exist if they do return true else return false
        if jsonObj['username'] == self.username and jsonObj['password'] == self.password:
            return True
        else:
            return False
