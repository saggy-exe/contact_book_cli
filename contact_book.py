import sqlite3
from contact import Contact

class ContactBook:
    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                name TEXT NOT NULL,
                phone TEXT PRIMARY KEY,
                email TEXT,
                added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    
    def add_contact(self, name, phone, email):
        try:
            self.cursor.execute("""
                INSERT INTO contacts (name, phone, email)
                VALUES (?, ?, ?)
            """, (name, phone, email))
            self.conn.commit()
            print("Contact added!")
        except sqlite3.IntegrityError:
            print("Phone number already exists.")

    
    def view_contacts(self):
        self.cursor.execute("SELECT name, phone, email, added_on FROM contacts")
        rows = self.cursor.fetchall()

        if not rows:
            print("No contacts found.")
            return

        for row in rows:
            contact = Contact(*row)
            print("\n" + str(contact))

    
    def search_contact(self, keyword):
        self.cursor.execute("""
            SELECT name, phone, email, added_on FROM contacts
            WHERE name LIKE ? OR phone LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

        results = self.cursor.fetchall()

        if not results:
            print("No matches found.")
            return

        for row in results:
            contact = Contact(*row)
            print("\n" + str(contact))

    
    def delete_contact(self, name):
        self.cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        self.conn.commit()

        if self.cursor.rowcount == 0:
            print("Contact not found.")
        else:
            print("Contact deleted.")

    
    def close(self):
        self.conn.close()