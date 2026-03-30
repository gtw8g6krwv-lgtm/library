class Book:
    def __init__(self, book_id: str, title: str, author: str, year: int):
        self.book_id = book_id
        self.title = title.strip()
        self.author = author.strip()
        self.year = year
        self.is_available = True
        self.current_holder = None