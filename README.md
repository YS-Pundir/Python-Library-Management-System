# 🏛️ Library Management System

**A Python OOP Project Built from Scratch | 12-Hour Challenge 🚀**

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white) 
![Status](https://img.shields.io/badge/Status-Complete-success) 
![License](https://img.shields.io/badge/License-MIT-green) 
![Built With Passion](https://img.shields.io/badge/Built_With-Passion-red)

A complete **Library Management System** demonstrating Python Object-Oriented Programming concepts with a fully functional **command-line interface**. This project showcases building a real-world system from scratch as a beginner in Python.

---

## 📌 Table of Contents

- [Features](#-features)  
- [Quick Start](#-quick-start)  
- [Architecture](#-architecture)  
- [Key Methods](#-key-methods)  
- [12-Hour Challenge](#-12-hour-challenge)  
- [What I Learned](#-what-i-learned)  
- [Future Improvements](#-future-improvements)  
- [About Me](#-about-me)  
- [License](#-license)  

---

## ✨ Features

| Feature | Status | Description |
|---------|--------|------------|
| 📚 Book Management | ✅ Complete | Add, remove, view, and search books |
| 👥 Member System | ✅ Complete | Register members and manage borrowing |
| 🔄 Borrow/Return | ✅ Complete | Full borrowing lifecycle with real-time updates |
| 🖥️ Interactive Menu | ✅ Complete | User-friendly command-line interface |
| 📊 Inventory Tracking | ✅ Complete | Track book availability and member activity |

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YS-Pundir/Python-Library-Management-System.git

# Navigate to project folder
cd Python-Library-Management-System

# Run the application
python library_system.py
First Run
markdown
Copy code
==============================
Welcome to City Central Library
==============================

1. Add Books   2. Remove Books
3. Add Members 4. Remove Members
5. Borrow Book 6. Return a Book
7. Show Books  8. Show Members
🏗️ Architecture
Core Classes
python
Copy code
class Book:
    """Represents individual books with title, author, ISBN"""

class Library:
    """Manages collection of books and operations"""

class Member(Library):
    """Extends Library to handle member operations"""
🛠️ Key Methods
addBooks() – Add books to the library

removeBooks() – Remove books from the library

registerMember() – Add new members

removeMember() – Remove members

borrowBook() – Borrow a book

returnBook() – Return a borrowed book

showBooks() – Display all available books

showMembers() – Display registered members

⏰ The 12-Hour Challenge
Hour	Task
1-2	Learned OOP & created Book class
3-4	Built Library class with main functions
5-6	Created Member class with inheritance
7-8	Built interactive menu system
9-10	Added borrow/return functionality
11-12	Debugged and made it fully functional

Completing this in 12 hours as a beginner shows fast learning, persistence, and the ability to deliver a complete system from scratch.

🧠 What I Learned
Python Object-Oriented Programming (OOP)

Classes, Objects, and Inheritance

Handling user input and validations

Building a complete system from scratch

Problem-solving independently and debugging

🔮 Future Improvements
Add file storage to save library and member data

Implement enhanced error handling

Improve search functionality

Create a GUI interface

Integrate with a database for persistence

👨‍💻 About Me
I’m Yuvraj Singh Pundir, a Python enthusiast learning step by step. This project marks my first fully functional Python OOP project built from scratch in just 12 hours!

GitHub: @YS-Pundir

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

"Built with passion in 12 hours of learning" ⏰🚀
