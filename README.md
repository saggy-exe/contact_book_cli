# 📇 Contact Book CLI (Python)

A clean, modular, command-line Contact Book application built with Python.
This project demonstrates solid **OOP design**, **SQL database operations**, and **input validation**, making it a great showcase for foundational backend skills.

---

## 🚀 Features

* ➕ **Add Contact**

  * Validates phone (10-digit numeric)
  * Validates email format (custom logic, no regex)

* 📋 **View Contacts**

  * Displays all contacts in a neatly formatted table
  * Sorted alphabetically by name

* 🔍 **Search Contacts**

  * Case-insensitive partial match on names

* ❌ **Delete Contact**

  * Removes contact by name

* 💾 **Persistent Storage**

  * Contacts saved in `contacts.db`
  * Automatically loaded on startup

* ⚠️ **Error Handling**

  * Gracefully handles missing data (`sqlite3.IntegrityError`)

---

## 🧠 Project Structure

```
contact-book/
│
├── contact.py        # Contact model
├── contact_book.py   # Core logic (ContactBook class)
├── main.py           # CLI interface
├── contacts.db       # Data storage (auto-created)
└── README.md
```

---

## 🏗️ Design Overview

### 🔹 Contact Class

Represents a single contact with:

* `name`
* `phone`
* `email`
* `added_on` (timestamp)

Includes:

* `__str__` for DB serialization

---

### 🔹 ContactBook Class

Acts as the brain of the application:

* Manages in-memory contact list
* Handles database management using SQLite
* Provides all core operations:

  * add
  * view
  * search
  * delete

---

### 🔹 main.py

Handles user interaction via CLI menu.

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/contact-book.git
cd contact-book
```

### 2. ▶️ Run the Application

```bash
python main.py
```

---

## 🖥️ Sample Menu

```
--- Contact Book ---
1. Add
2. View
3. Search
4. Delete
5. Quit
```

---

## 🧪 Validation Rules

### Phone

* Must contain only digits
* Must be exactly 10 digits

### Email

* Exactly one `@`
* Valid domain structure
* No consecutive dots
* Proper extension (e.g. `.com`, `.in`)


---

## 🎯 Learning Outcomes

This project demonstrates:

* Object-Oriented Programming (OOP)
* Database operations using SQLite
* Input validation without regex
* Clean code structure and modularity
* CLI application design

---

## 👨‍💻 Author

**Sagnic Ghosh**

---

If you found this project useful or interesting, feel free to ⭐ the repository!
