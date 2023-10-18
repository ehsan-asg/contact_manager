import pickle
import os
directory_path = "contact-manager/contact_maneager/data/"
file_path_user = os.path.join(directory_path, "users.pikle")


class User:
    def __init__(self, list_users) -> None:
        self.save_users = list_users

    def create_user(self, username, password):
        if username in self.save_users.keys():
            return "User not created"
        self.username = username
        self.password = password
        self.save_users[username] = password
        self.__save_pickle()
        return "User created successfully"

    def authenticate_user(self, username, passwd_user):
        if username in self.save_users.keys():
            if passwd_user in self.save_users.values():
                return "login susscful"
        return "not validate"

    def modifyin_user(self, new_password):
        self.password = new_password
        return "change password"

    def __save_pickle(self):
        with open(file_path_user, 'wb') as handle:
            pickle.dump(self.save_users, handle,
                        protocol=pickle.HIGHEST_PROTOCOL)
