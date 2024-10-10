class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
class Library :
    def __init__(self):
        self._books = []
    def add_book(self, Book):
        self._books.append(Book)
    def check_out_book(self, Book):
        for book in self._books:
            if book.title == Book:

                self._books.remove(Book)
                self._is_checked_out = True
                break

    def return_book(self, Book):
        self._books.append(Book)
        return True
    def list_available_books(self):
        for book in self._books:
            print(book)
