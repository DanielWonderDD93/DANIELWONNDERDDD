# operations.py
# Daniel's Smart Library Management System
# Version: Simple and procedural

books = {}  # key = ISBN, value = dict(title, author, genre, copies)
members = []  # list of dicts
genres = ("Fiction", "Non-Fiction", "Science", "Technology")

# ---------- Book Functions ---------- #

def add_book(isbn, title, author, genre, copies):
    if isbn in books:
        return "Book already exists!"
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total": copies,
        "available": copies
    }
    return f"Book '{title}' added."


def search_books(term):
    result = []
    for k, v in books.items():
        if term.lower() in v["title"].lower() or term.lower() in v["author"].lower():
            result.append({k: v})
    return result if result else "No matches found."


def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available"] < books[isbn]["total"]:
        return "Some copies are borrowed; cannot delete."
    del books[isbn]
    return f"Book {isbn} deleted."


# ---------- Member Functions ---------- #

def add_member(member_id, name, email):
    for m in members:
        if m["id"] == member_id:
            return "Member ID exists."
    members.append({
        "id": member_id,
        "name": name,
        "email": email,
        "borrowed": []
    })
    return f"Member {name} added."


def delete_member(member_id):
    for m in members:
        if m["id"] == member_id:
            if m["borrowed"]:
                return "Return books first!"
            members.remove(m)
            return f"Member {m['name']} deleted."
    return "Member not found."


# ---------- Borrow / Return ---------- #

def borrow_book(member_id, isbn):
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available"] <= 0:
        return "No copies left."

    for m in members:
        if m["id"] == member_id:
            m["borrowed"].append(isbn)
            books[isbn]["available"] -= 1
            return f"{m['name']} borrowed '{books[isbn]['title']}'."
    return "Member not found."


def return_book(member_id, isbn):
    for m in members:
        if m["id"] == member_id:
            if isbn in m["borrowed"]:
                m["borrowed"].remove(isbn)
                books[isbn]["available"] += 1
                return f"{m['name']} returned '{books[isbn]['title']}'."
            return "Book not borrowed by this member."
    return "Member not found."
