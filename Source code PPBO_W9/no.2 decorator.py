class Book:
    GENRES = ('Fiction', 'Non-Fiction', 'Fantasy', 'Science', 'Mystery')

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self): # instance method
        return f"{self.title} by {self.author}, {self.pages} pages"

    @property
    def short_description(self): # property method
        return f"{self.title} - {self.author}"

    @classmethod
    def genres_starting_with(cls, char): # class method
        return [g for g in cls.GENRES if g.startswith(char)]

    @staticmethod
    def is_lengthy(pages): # static method
        return pages > 300

# Contoh penggunaan
book1 = Book("The Great Adventure", "Alice Walker", 350)

print(book1.description())
print(book1.short_description)

print(book1.genres_starting_with("F"))
print(book1.genres_starting_with("S"))

print(Book.is_lengthy(150))
print(Book.is_lengthy(book1.pages))