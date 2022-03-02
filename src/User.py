from .models_gurlllll.ModelUser import UserModel

class UserController:
    def __init__(self):
        print("L to login")
        print("Q to quit")

        input_option = input("Please select an option: ")

        if input_option == "L":
            self.login()
        elif input_option == "Q":
            exit(0x45)
        else:
            print("Invalid option")
            self.__init__()


    def login(self):
        # Give the user 3 tries to login
        for i in range(3):
            username = input("Username: ")
            password = input("Password: ")

            # Check if the password is correct and the user exists
            user = UserModel(username, password).findByUsername()

            # If the password is correct and the user exists log them in
            if user:
                print("Welcome {}".format(username))
                break
            else:
                #Another attempt babby
                print("Invalid username or password")
