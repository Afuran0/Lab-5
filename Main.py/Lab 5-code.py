class Book:
    def __init__(self, title, author, pages):
        # Initialize book attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False  

    def description(self):
        # Return book details
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def mark_as_read(self):
        # Mark the book as read and print a message
        self.read = True
        print(f"You have marked '{self.title}' as read.")

class EbookReader:
    def __init__(self):
        # Predefined list of available books
        self.available_books = [
            Book("The Little Liar", "Mitch Albom", 279),
            Book("Moby Dick", "Herman Melville", 635),
            Book("The Hunger Games", "Suzanne Collins", 358),
            Book("Frankenstein", "Mary Shelley", 280),
            Book("The Keeper", "Buck Turner", 320),
        ]
        self.purchased_books = []  

    def display_available_books(self):
        # Print the list of available books
        print("Available Books:")
        for index, book in enumerate(self.available_books):
            print(f"{index + 1}. {book.description()}")

    def buy_book(self, index):
        # Buy a book by index
        if 0 <= index < len(self.available_books):
            # Remove from available
            book = self.available_books.pop(index) 
            # Add to purchased list
            self.purchased_books.append(book)  
            print(f"You have purchased '{book.title}'.")
        else:
            print("Invalid book index.")

    def view_purchased_books(self):
        # Print the list of purchased books
        if not self.purchased_books:
            print("You have not purchased any books yet.")
            return
        print("Your Purchased Books:")
        for book in self.purchased_books:
            print(book.description())

    def read_book(self, index):
        # Mark purchased books as read 
        if 0 <= index < len(self.purchased_books):
            book = self.purchased_books[index]
            book.mark_as_read()
        else:
            print("Invalid book index.")

def main():
    reader = EbookReader()  
    
    while True:
        # Display menu options
        print("\nE-Book Reader Menu:")
        print("1. Display Available Books")
        print("2. Buy a Book")
        print("3. View Purchased Books")
        print("4. Read a Book")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            # Show available books
            reader.display_available_books()  
        elif choice == '2':
            reader.display_available_books()  
            book_index = int(input("Enter the number of the book you want to buy: ")) - 1
            # Buy the selected book
            reader.buy_book(book_index)  
        elif choice == '3':
            # Show purchased books
            reader.view_purchased_books()  
        elif choice == '4':
            reader.view_purchased_books()  
            book_index = int(input("Enter the number of the book you want to read: ")) - 1
            # Read the selected book
            reader.read_book(book_index)  
        elif choice == '5':
            # Exit 
            print("Exiting the e-book reader.")  
            break
        else:
            # Error message 
            print("Invalid option, please try again.")  

# Run the main function
if __name__ == "__main__":
    main()  
