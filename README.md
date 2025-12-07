🏛️ Library Management System

A Python OOP Project Built from Scratch | 12-Hour Challenge 🚀

A complete Library Management System demonstrating Python Object-Oriented Programming concepts with a fully functional command-line interface.

✨ Features
Feature	Status	Description
📚 Book Management	✅ Complete	Add, remove, view, and search books
👥 Member System	✅ Complete	Register members and manage borrowing
🔄 Borrow/Return	✅ Complete	Track book borrowing and returns
🖥️ Interactive Menu	✅ Complete	User-friendly command-line interface
📊 Inventory Tracking	✅ Complete	Real-time book availability
🚀 Quick Start
Installation
# Clone the repository
git clone https://github.com/YS-Pundir/Python-Library-Management-System.git

# Navigate to project folder
cd Python-Library-Management-System

# Run the application
python library_system.py

First Run
==============================
Welcome to City Central Library
==============================

1. Add Books   2. Remove Books
3. Add Members 4. Remove Members
5. Borrow Book 6. Return a Book
7. Show Books  8. Show Members

🏗️ Architecture
Core Classes
class Book:
    """Represents individual books with title, author, ISBN"""

class Library:
    """Manages collection of books and operations"""

class Member(Library):
    """Extends Library to handle member operations"""

Key Methods

addBooks() – Add multiple books to inventory

removeBooks() – Remove books from library

registerMember() – Add new members

removeMember() – Remove existing members

borrowBook() – Borrow a book

returnBook() – Return a borrowed book

showBooks() – Display available books

showMembers() – Display registered members

⏰ The 12-Hour Challenge
Hour	Task
1-2	Learned OOP & created Book class
3-4	Built Library class with main functions
5-6	Created Member class with inheritance
7-8	Built interactive menu system
9-10	Added borrow/return functionality
11-12	Debugged and made it WORK!
🧠 What I Learned

Python Object-Oriented Programming

Classes, Objects, and Inheritance

Handling user input

Building a complete system from scratch

Problem-solving independently

🔮 Future Improvements

Add file storage to save library and member data

Implement better error handling

Enhance search functionality

Add GUI interface

Integrate with a database

👨‍💻 About Me

I’m Yuvraj Singh Pundir, a Python enthusiast learning step by step. This project marks my first fully functional Python OOP project built from scratch in just 12 hours!

GitHub: @YS-Pundir

📄 License

This project is licensed under the MIT License – feel free to learn from it and build upon it!

"Built with passion in 12 hours of learning" ⏰🚀
