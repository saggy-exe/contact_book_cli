import datetime 

class Contact:
    def __init__(self, name, phone, email, added_on=None):
        self.name = name
        self.phone = phone
        self.email = email

        if added_on:
            self.added_on = added_on
        else:
            current = datetime.datetime.now()
            self.added_on = datetime.datetime.strftime(current, "%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "added_on": self.added_on
        }
    