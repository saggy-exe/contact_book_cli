import json
from contact import Contact

class ContactBook:

    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []

        self.load_contacts()


    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.contacts = [
                    Contact(
                        entry["name"],
                        entry["phone"],
                        entry["email"],
                        entry["added_on"]
                    )
                    for entry in data
                ]
        except FileNotFoundError:
            self.contacts = []


    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)


    def is_valid_phone(self, phone):
        return phone.isdigit() and len(phone) == 10


    def is_valid_email(self, email):
        # Must contain exactly one '@'
        if email.count("@") != 1:
            return False
        
        local, domain = email.split("@")
        
        # Basic non-empty checks
        if not local or not domain:
            return False
        
        # No starting or ending dot
        if local.startswith(".") or local.endswith("."):
            return False
        
        # No consecutive dots
        if ".." in local or ".." in domain:
            return False
        
        # Domain must contain at least one dot
        if "." not in domain:
            return False
        
        # Split domain into name + extension
        domain_name, extension = domain.rsplit(".", 1)
        
        # Extension must be at least 2 letters
        if len(extension) < 2 or not extension.isalpha():
            return False
        
        # Domain rules
        if domain_name.startswith("-") or domain_name.endswith("-"):
            return False
        
        # Allowed characters (basic)
        allowed_local = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-")
        allowed_domain = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-")
        
        if not all(c in allowed_local for c in local):
            return False
        
        if not all(c in allowed_domain for c in domain):
            return False
        
        return True


    def add_contact(self, name, phone, email):
        if not self.is_valid_phone(phone):
            print("Invalid phone number.")
            return
        
        if not self.is_valid_email(email):
            print("Invalid email.")
            return

        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print("Contact added successfully.")


    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        sorted_contacts = sorted(self.contacts, key=lambda c: c.name.lower())

        print(f"{'Name':<20} {'Phone':<15} {'Email':<30} {'Added On'}")
        print("-" * 75)

        for c in sorted_contacts:
            print(f"{c.name:<20} {c.phone:<15} {c.email:<30} {c.added_on}")


    def search_contact(self, query):
        results = [
            c for c in self.contacts
            if query.lower() in c.name.lower()
        ]

        if not results:
            print("No matching contacts found.")
            return

        for c in results:
            print(f"{c.name} | {c.phone} | {c.email}")


    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                print("Contact deleted.")
                return
        
        print("Contact not found.")
