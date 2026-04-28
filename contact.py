import datetime 

class Contact:
    def __init__(self, name, phone, email, added_on=None):
        self.name = name
        self.phone = phone
        self.email = email

        self.added_on = added_on or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Email: {self.email}\n"
            f"Added on: {self.added_on}"
        )