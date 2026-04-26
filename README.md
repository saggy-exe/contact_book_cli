# 📇 Contact Book CLI (Python)

A clean, modular, command-line Contact Book application built with Python.
This project demonstrates solid **OOP design**, **file persistence**, and **input validation**, making it a great showcase for foundational backend skills.

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

  * Contacts saved in `contacts.json`
  * Automatically loaded on startup

* ⚠️ **Error Handling**

  * Gracefully handles missing files (`FileNotFoundError`)

---

## 🧠 Project Structure

```
contact-book/
│
├── contact.py        # Contact model
├── contact_book.py   # Core logic (ContactBook class)
├── main.py           # CLI interface
├── contacts.json     # Data storage (auto-created)
├── requirements.txt  # Dependencies (minimal)
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

* `to_dict()` for JSON serialization

---

### 🔹 ContactBook Class

Acts as the brain of the application:

* Manages in-memory contact list
* Handles file I/O (load/save)
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

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

> Note: This project uses only Python standard library, so requirements may be empty.

---

## ▶️ Running the Application

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

## 📦 Example `contacts.json`

```json
[
    {
        "name": "Aarav Sharma",
        "phone": "9876543210",
        "email": "aarav.sharma@example.com",
        "added_on": "2026-04-20 10:15:30"
    }
]
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

## 🌱 Future Improvements

* ✏️ Update contact feature
* 🚫 Prevent duplicate entries
* 📤 Export contacts to CSV
* 🧾 Pretty tables using `tabulate`
* 🧪 Unit tests with `pytest`
* 🔐 Data encryption for sensitive info

---

## 🎯 Learning Outcomes

This project demonstrates:

* Object-Oriented Programming (OOP)
* File handling with JSON
* Input validation without regex
* Clean code structure and modularity
* CLI application design

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Sagnic Ghosh**

---

If you found this project useful or interesting, feel free to ⭐ the repository!
