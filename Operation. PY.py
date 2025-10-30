"""Class-based in-memory library operations.

This module exposes the same function names expected by the test
script `Balu` but provides a clearer, tested implementation.

Design notes:
- Books and members stored in module-level dicts so imports behave
  same as before.
- Borrow limit per member = 3.
- Allowed genres include Fiction and Non-Fiction.
"""

from typing import Dict, Set

ALLOWED_GENRES = {"Fiction", "Non-Fiction", "Science", "Biography"}


class Book:
    def __init__(self, isbn: str, title: str, author: str, genre: str, total_copies: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        self.borrowed = 0


class Member:
    def __init__(self, mid: str, name: str, email: str):
        self.mid = mid
        self.name = name
        self.email = email
        self.borrowed: Set[str] = set()


# Module-level storage to keep previous API shape
books: Dict[str, Book] = {}
members: Dict[str, Member] = {}


def _valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    return local != "" and "." in domain


def add_book(isbn, title, author, genre, total_copies):
    if not isinstance(isbn, str):
        return False
    if isbn in books:
        return False
    if not all(isinstance(x, str) and x.strip() for x in (title, author)):
        return False
    if not isinstance(genre, str) or genre not in ALLOWED_GENRES:
        return False
    if not isinstance(total_copies, int) or total_copies < 0:
        return False
    books[isbn] = Book(isbn, title, author, genre, total_copies)
    return True


def add_member(mid, name, email):
    if not isinstance(mid, str):
        return False
    if mid in members:
        return False
    if not isinstance(name, str) or name.strip() == "":
        return False
    if not _valid_email(email):
        return False
    members[mid] = Member(mid, name, email)
    return True


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return False
    b = books[isbn]
    if title is not None:
        if not isinstance(title, str) or title.strip() == "":
            return False
        b.title = title
    if author is not None:
        if not isinstance(author, str) or author.strip() == "":
            return False
        b.author = author
    if genre is not None:
        if not isinstance(genre, str) or genre not in ALLOWED_GENRES:
            return False
        b.genre = genre
    if total_copies is not None:
        if not isinstance(total_copies, int) or total_copies < 0:
            return False
        if total_copies < b.borrowed:
            return False
        b.total_copies = total_copies
    return True


def update_member(mid, name=None, email=None):
    if mid not in members:
        return False
    m = members[mid]
    if name is not None:
        if not isinstance(name, str) or name.strip() == "":
            return False
        m.name = name
    if email is not None:
        if not _valid_email(email):
            return False
        m.email = email
    return True


def search_books(query, by="title"):
    if by not in ("title", "author"):
        return False
    q = str(query).lower()
    for b in books.values():
        if by == "title" and q in b.title.lower():
            return True
        if by == "author" and q in b.author.lower():
            return True
    return False


def delete_book(isbn):
    if isbn not in books:
        return False
    b = books[isbn]
    if b.borrowed > 0:
        return False
    del books[isbn]
    return True


def delete_member(mid):
    if mid not in members:
        return False
    m = members[mid]
    if len(m.borrowed) > 0:
        return False
    del members[mid]
    return True


def borrow_book(isbn, mid):
    # validations
    if isbn not in books:
        return False
    if mid not in members:
        return False
    b = books[isbn]
    m = members[mid]
    # already borrowed by this member
    if isbn in m.borrowed:
        return False
    # no copies available
    if b.borrowed >= b.total_copies:
        return False
    # member reached limit
    if len(m.borrowed) >= 3:
        return False
    b.borrowed += 1
    m.borrowed.add(isbn)
    return True


def return_book(isbn, mid):
    if isbn not in books:
        return False
    if mid not in members:
        return False
    b = books[isbn]
    m = members[mid]
    if isbn not in m.borrowed:
        return False
    m.borrowed.remove(isbn)
    b.borrowed -= 1
    return True
