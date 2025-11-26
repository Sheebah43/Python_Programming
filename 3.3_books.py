# Check  list of   books. Allow user to
# Issue a book
# Return a book
# Check list
# Impose fine @Re 1 after 15 days
# View available books


from datetime import date, datetime, timedelta

books_list = [
    {"id": 1, "title": "Book 1", "author": "abc", "total": 12, "issued": 0},
    {"id": 2, "title": "Book 2", "author": "def", "total": 9, "issued": 0},
    {"id": 3, "title": "Book 3", "author": "ghi", "total": 6, "issued": 0},
]

issued = []


def available_copies(b):
    return b["total"] - b["issued"]

def find_book(book_id):
    for b in books_list:
        if b["id"] == book_id:
            return b
    return None

def list_all_books():
    print("\nAll books:")
    for b in books_list:
        print(f"{b['id']}. {b['title']} by {b['author']} (Total: {b['total']}, Issued: {b['issued']})")

def list_available():
    print("\nAvailable books:")
    for b in books_list:
        av = available_copies(b)
        if av > 0:
            print(f"{b['id']}. {b['title']} (Available: {av})")

def issue_book():
    try:
        bid = int(input("Enter book id to issue: ").strip())
    except ValueError:
        print("Invalid id")
        return
    book = find_book(bid)
    if not book:
        print("Book not found")
        return
    if available_copies(book) <= 0:
        print("No copies available")
        return
    user = input("Enter your name: ").strip()

    book["issued"] += 1
    issued.append({"book_id": bid, "user": user, "issue_date": date.today()})
    print(f"Issued '{book['title']}' to {user} on {date.today()}")

def return_book():
    try:
        bid = int(input("Enter book id to return: ").strip())
    except ValueError:
        print("Invalid id")
        return
    user = input("Enter your name: ").strip()
    # find the first matching issued record
    for i, rec in enumerate(issued):
        if rec["book_id"] == bid and rec["user"].lower() == user.lower():
            issue_dt = rec["issue_date"]
            days = (date.today() - issue_dt).days
            overdue = max(0, days - 15)
            fine = overdue  # Re 1 per day
            # update counts and remove record
            book = find_book(bid)
            if book:
                book["issued"] = max(0, book["issued"] - 1)
            issued.pop(i)
            print(f"Returned '{book['title']}' by {user}. Borrowed days: {days}. Fine: Rs {fine}")
            return
    print("No matching issued record found")

def menu():
    while True:
        print("\nChoose 1) List all  2) View available  3) Issue  4) Return  5) View issued  6) Quit")
        ch = input("Choose: ").strip()
        if ch == "1":
            list_all_books()
        elif ch == "2":
            list_available()
        elif ch == "3":
            issue_book()
        elif ch == "4":
            return_book()
        elif ch == "5":
            print("\nCurrently issued:")
            if not issued:
                print("None")
            for rec in issued:
                print(f"Book {rec['book_id']} to {rec['user']} on {rec['issue_date']}")
        elif ch == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
