# demo.py
# Demo for Daniel’s Smart Library Management System
from operations import *

# Add books
print(add_book("B101", "Python Made Easy", "John Code", "Technology", 3))
print(add_book("B102", "World of Science", "Marie Lynn", "Science", 2))
print(add_book("B103", "Think and Grow Rich", "Napoleon Hill", "Non-Fiction", 4))

# Add members
print(add_member("D001", "Daniel Brown", "daniel@example.com"))
print(add_member("D002", "Grace Smart", "grace@example.com"))

# Borrow and return
print(borrow_book("D001", "B101"))
print(borrow_book("D001", "B102"))
print(return_book("D001", "B101"))

# Search
print("Search result for 'Python':", search_books("Python"))

# Delete records
print(delete_book("B103"))
print(delete_member("D002"))

# Final Data
print("\nBooks:", books)
print("Members:", members)
