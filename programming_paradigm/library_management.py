class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = false
class library :
    def __init__(self, book):
        self._books = []
    def add_book(self):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                break
        for book in self._books :
            print(book)

