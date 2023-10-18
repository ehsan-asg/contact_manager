from contacts import Contact
from validators import Validate
from users import User
import csv
import pickle
import os
directory_path = "contact-manager/contact_maneager/data/"
file_path_contacts = os.path.join(directory_path, "contacts.pikle")
file_path_user = os.path.join(directory_path, "users.pikle")
try:
    with open(file_path_contacts, 'rb') as handle:
        list_contact = pickle.load(handle)
    with open(file_path_user, 'rb') as handle:
        list_user = pickle.load(handle)
except (FileNotFoundError, EOFError):
    list_contact = {}
    list_user = {}


class Management:
    def __init__(self, list_contact, list_user):
        self.save_contact = list_contact
        self.save_user = list_user
        self.list_key = self.save_contact.keys()
        self.contact = Contact()

    def add_contact(self, name, email, phone):

        if Validate.is_valid_email(email) and Validate.is_phone_number(phone):
            self.contact.create_contact(name, email, phone)
            return "contact created successfully"
            # if name in self.list_key:
            #     return "not is valid"

        # return "Your mobile number or email was entered incorrectly"

    def edit_contact(self, name, email, phone):

        if Validate.is_phone_number(phone) and Validate.is_valid_email(email):
            if name in self.list_key:
                return ("not is valid")
            self.contact.edit_user(name, email, phone)

    def delete_contact(self, name):
        if name in self.list_key:
            return self.contact.delete_user(name)

    def display_user(self):
        for item in self.save_contact:
            print(item)

    def create_csv(self, filename):
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "Name", "Subject"])
            for item in self.save_contact:
                writer.writerow([1, "Ash Ketchum", "English"])
                writer.writerow([2, "Gary Oak", "Mathematics"])
                writer.writerow([3, "Brock Lesner", "Physics"])


user = User(list_user)
# while True:
#     print("""
# 1.create user
# 2.login user
#         """)
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         username = input("enter username : ")
#         password = input("enter password : ")
#         print(user.create_user(username, password))

#     elif choice == "2":
#         print(list_user)
#         username = input("enter username : ")
#         password = input("enter password : ")
#         print(user.authenticate_user(username, password))
#         break
contact = Management(list_contact, list_user)
while True:
    print("""
1 Add a new contact
2 Edit an existing contact
3 Delete a contact
4 View all contacts
5 Quit
        """)
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("enter name : ")
        email = input("enter email : ")
        phone = input("enter phone number : ")
        print(contact.add_contact(name, email, phone))
    elif choice == "2":
        name = input("enter name : ")
        email = input("enter email : ")
        phone = input("enter phone number : ")
        print(contact.edit_contact(name, email, phone))
    elif choice == "3":
        name = input("enter name : ")

        print(contact.delete_contact(name))
