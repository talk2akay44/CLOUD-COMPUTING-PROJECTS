# Online Bookstore Management System

inventory = [
    {"id": 1, "title": "Atomic Habits", "author": "James Clear", "price": 2000.00, "quantity": 5},
    {"id": 2, "title": "Richest Man in Babylon", "author": "George Clason", "price": 1500, "quantity": 2},
    {"id": 1, "title": "Think and Grow Rich", "author": "Napoleon Hill", "price": 2000.00, "quantity": 3},
    {"id": 1, "title": "Half of a Yellow Sun", "author": "Chimamanda Ngozi Adichie", "price": 3000.00, "quantity": 10},
    {"id": 2, "title": "Things Fall Apart", "author": "Chinua Achebe", "price": 3500, "quantity": 7},
]

# Staff Users
staff_users = {
    "admin": "admin123",
    "Akay": "akay123",
    "Shevy": "shevy234"
}

# Function to authenticate staff members
def authenticate_staff(username, password):
    if username in staff_users and staff_users[username] == password:
        return True
    else:
        return False

# Function to add a book to the inventory
def add_book(inventory, title, author, price, quantity):
    new_id = len(inventory) + 1
    inventory.append({"id": new_id, "title": title, "author": author, "price": price, "quantity": quantity})
    print(f"Book '{title}' added successfully!")

# Function to remove a book from the inventory
def remove_book(inventory, book_id):
    for book in inventory:
        if book["id"] == book_id:
            inventory.remove(book)
            print(f"Book with ID {book_id} removed successfully!")
            return
    print(f"No book found with ID {book_id}.")

# Function to update book information in the inventory
def update_book(inventory, book_id, title=None, author=None, price=None, quantity=None):
    for book in inventory:
        if book["id"] == book_id:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if price:
                book["price"] = price
            if quantity:
                book["quantity"] = quantity
            print(f"Book with ID {book_id} updated successfully!")
            return
    print(f"No book found with ID {book_id}.")

# Function to search for books in the inventory
def search_books(inventory, search_term):
    results = [book for book in inventory if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
    return results

# Function to view details of a specific book
def view_book_details(book):
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Price: ${book['price']}, Quantity: {book['quantity']}")

# Function to purchase a book from the inventory
def purchase_book(inventory, book_id):
    for book in inventory:
        if book["id"] == book_id:
            if book["quantity"] > 0:
                book["quantity"] -= 1
                print(f"Thank you for purchasing '{book['title']}'!")
                return
            else:
                print(f"Sorry, '{book['title']}' is out of stock.")
                return
    print(f"No book found with ID {book_id}.")

# Main program loop
def main():
    while True:
        user_type = input("Are you a (1) Staff or (2) Customer? (Enter 1 or 2): ")
        
        if user_type == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            if authenticate_staff(username, password):
                print("Welcome, staff member!")
                while True:
                    action = input("Choose an action: (1) Add Book (2) Remove Book (3) Update Book (4) Logout: ")
                    if action == "1":
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        price = float(input("Enter book price: "))
                        quantity = int(input("Enter book quantity: "))
                        add_book(inventory, title, author, price, quantity)
                    elif action == "2":
                        book_id = int(input("Enter book ID to remove: "))
                        remove_book(inventory, book_id)
                    elif action == "3":
                        book_id = int(input("Enter book ID to update: "))
                        title = input("Enter new title (leave blank to keep current): ")
                        author = input("Enter new author (leave blank to keep current): ")
                        price = input("Enter new price (leave blank to keep current): ")
                        quantity = input("Enter new quantity (leave blank to keep current): ")
                        update_book(inventory, book_id, title or None, author or None, float(price) if price else None, int(quantity) if quantity else None)
                    elif action == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid action. Please try again.")
            else:
                print("Invalid username or password. Please try again.")
        
        elif user_type == "2":
            print("Welcome, customer!")
            while True:
                action = input("Choose an action: (1) Search Books (2) Purchase Book (3) Exit: ")
                if action == "1":
                    search_term = input("Enter a search term (title or author): ")
                    results = search_books(inventory, search_term)
                    if results:
                        for book in results:
                            view_book_details(book)
                    else:
                        print("No books found matching your search.")
                elif action == "2":
                    book_id = int(input("Enter book ID to purchase: "))
                    purchase_book(inventory, book_id)
                elif action == "3":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid action. Please try again.")
        
        else:
            print("Invalid user type. Please enter 1 for Staff or 2 for Customer.")

if __name__ == "__main__":
    main()