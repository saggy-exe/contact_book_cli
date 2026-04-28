from contact_book import ContactBook

def main():
    book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Delete")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            query = input("Search name: ")
            book.search_contact(query)

        elif choice == "4":
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "5":
            book.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()