"""
tests.py
Unit tests for Mini Library Management System
Author: [Daniel Amara Brima]
Module: PROG211 Object-Oriented Programming 1
"""

from operations import (
    GENRES, books, members,
    add_book, add_member,
    update_book, update_member,
    delete_book, delete_member,
    borrow_book, return_book
)

# Clear all global data before testing
books.clear()
members.clear()

print("===== RUNNING LIBRARY SYSTEM TESTS =====")

# ⿡ Test: Add a book
assert add_book("B001", "Merchant of venice", "Daniel", "Non-Fiction", 5) == True, "Failed to add valid book"
assert add_book("B001", "Far from Home", "Argu", "Fiction", 3) == False, " Duplicate ISBN should fail"
assert add_book("B002", "The Church Girl", "Elysia", "Romance", 2) == False, " Invalid genre should fail"
print(" add_book() passed")

# ⿢ Test: Add a member
assert add_member("M001", "Kallon", "Kallon@example.com") == True, " Failed to add member"
assert add_member("M001", "Duplicate", "dup@example.com") == False, "Duplicate member ID should fail"
print(" add_member() passed")

# ⿣ Test: Update book & member
assert update_book("B001", title="Merchant of Venice for secondary level") == True, " Book update failed"
assert update_book("B259", title="Invalid") == False, "Nonexistent book update should fail"
assert update_member("M001", email="@example.com") == True, " Member update failed"
print(" update_book() & update_member() passed")

# ⿤ Test: Borrow and return
add_book("B003", "The Cage Birds Song ", "Haja", "Mystery", 1)
add_member("M002", "Grace", "Grace@example.com")

assert borrow_book("B003", "M002") == True, " Borrow should work when available"
assert borrow_book("B003", "M002") == False, " Cannot borrow if no copies left"
assert return_book("B003", "M002") == True, " Return should work"
assert return_book("B003", "M002") == False, " Cannot return a non-borrowed book"
print("borrow_book() & return_book() passed")

# ⿥ Test: Delete operations
assert delete_book("B003") == True, " Should delete returned book"
assert delete_member("M001") == True, " Should delete member with no borrowed books"
print("delete_book() & delete_member() passed")

print("\n ALL TESTS PASSED SUCCESSFULLY")
