import re


class Validate:
    @staticmethod
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True
        else:
            return False

    def is_phone_number(number):
        pattern = r"^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$"
        if re.match(pattern, number):
            return True
        else:
            return False
