from .models_gurlllll.ModelUser import UserModel

class UserController:
    def __init__(self):
        print("L to login")
        print("Q to quit")

        input_option = input("Please select an option: ")

        if input_option == "L":
            self.login()
        elif input_option == "Q":
            exit()
        else:
            print("Invalid option")
            self.__init__()


    def login(self):
        print("Login")
        username: str = input("Username: ")
        password: str = input("Password: ")

        user = UserModel(username, password).findByUsername()

        if user:
            print("Welcome", username)
        else:
            print("Wrong credentials")

        self.__init__()
