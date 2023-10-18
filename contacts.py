import pickle


class Contact:
    def __init__(self):
        self.contacts = {}

    def create_contact(self, name, email, phone):
        if name in self.contacts:
            self.contacts[name] = {'email': email, 'phone': phone}
            self.__save_contacts()
            return "contact created successfully"
        return "User not created"

    def edit_user(self, name, email, phone):
        self.save_user[name][email] = email
        self.save_user[name][phone] = phone
        self.__save_pickle()
        return "edit susscful"

    def delete_user(self, name):
        self.save_contact.pop(name)
        self.__save_pickle()
        return "The contact was deleted successfully"

    def __save_pickle(self):
        with open('data/contatcs.pikle', 'wb') as handle:
            pickle.dump(self.save_contact, handle,
                        protocol=pickle.HIGHEST_PROTOCOL)
