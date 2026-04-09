class Book:
    def __init__(self, book_id: str, title: str, author: str, year: int):
        self.__book_id = book_id
        self.__title = title.strip()
        self.__author = author.strip()
        self.__year = year
        self.__is_available = True
        self.__current_holder = None