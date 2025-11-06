# test_library.py
from operations import *

def run_tests():
    print("Running Tests for Daniel's Library System...\n")

    assert "added" in add_book("T001", "Test Book", "Tester", "Science", 2)
    assert "added" in add_member("M001", "Tester User", "tester@example.com")
    assert "borrowed" in borrow_book("M001", "T001")
    assert "returned" in return_book("M001", "T001")
    assert "deleted" in delete_book("T001")
    assert "deleted" in delete_member("M001")

    print("✅ All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
