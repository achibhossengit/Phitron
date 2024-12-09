class Library:
    book_list = []

    @classmethod # to access without creating object
    def entry_book(self, book):
        self.book_list.append(book)
    
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.__author = author
        self.availability = True
        Library.entry_book(self) # এখানে self হল বর্তমান Book অবজেক্ট, যেটি মাত্র তৈরি হয়েছে।

    @classmethod
    def view_book_info(self):
        for book in Library.book_list:
            print(f'ID: {book.book_id}, Title: {book.title}, Author: {book.__author}, Availability: {'Available' if book.availability else 'Not Available'}')

    @classmethod
    def borrow_book(self, book_id):
        valid = False
        for book in Library.book_list:
            if book.book_id == book_id:
                valid = True
                if book.availability == False:
                    print(f'"{book.title}" is already taken.')
                else:
                    print(f'"{book.title}" is borrowed successfully.')
                    book.availability = False
                break
        if valid == False:
            print(f'{book_id} is invalid. Please enter a valid book id.')
    
    @classmethod
    def return_book(self, book_id):
        valid = False
        for book in Library.book_list:
            if book.book_id == book_id:
                valid = True
                if book.availability:
                    print(f'You did\'t borrow "{book.title}"')
                else:
                    print(f'"{book.title}" return successfully.')
                    book.availability = True
        

# Adding Books in book list
Book(101, "Atomic Habit", "James Clear")
Book(102, "The Alchemist", "Paolo Coyelho")
Book(104, "The lean Startup", "Eric Ries")
Book(103, "Guide to Success", "Julia Seton")
Book(105, "Macine learning", "Stephen Kobri")
Book(106, "Fell Good Prod.", "Ali Abdal")


while True:
    print('\n🌸-----Welcome To the Libarary------🌸')
    n = int(input('1. View All Books\n2. Borrow Book\n3. Return Book\n4. Exit\n\nEnter Your choice: '))
    print()
    if n == 1:
        Book.view_book_info()
    elif n==2:
        id = int(input('Enter book ID to borrow: '))
        Book.borrow_book(id)
    elif n==3:
        id = int(input('Enter book ID to return: '))
        Book.return_book(id)
    else:
        break
