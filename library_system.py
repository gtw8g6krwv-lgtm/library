from messages import Messages
from book import Book


class Library:
    def __init__(self):
        self.__catalog_books = []
        self.__books_counter = 0

    def add_book_to_catalog(self, book_title: str, book_author: str, book_publication_year: str):
        self.__books_counter += 1
        book_id = f"{self.__books_counter:04d}"

        new_book = {
            "book_id": book_id,
            "title": book_title.strip(),
            "author": book_author.strip(),
            "year": book_publication_year,
            "is_available": True,
            "current_holder": None
        }

        self.__catalog_books.append(new_book)
        print(Messages.BOOK_ADDED.format(book_id))
        return book_id

    def find_book_by_id(self, book_id: str):
        for book in self.__catalog_books:
            if book["book_id"] == book_id:
                return book
        return None

    def find_book_by_title(self, title: str):
        for book in self.__catalog_books:
            if book["title"].lower() == title.lower():
                return book
        return None

    def find_book(self, search_query: str):
        book = self.find_book_by_id(search_query)
        if book:
            return book
        return self.find_book_by_title(search_query)

    def loan_book(self, book_identifier: str):
        book = self.find_book(book_identifier)
        library_reader_role = "Читатель"

        if not book:
            print(Messages.BOOK_NOT_FOUND)
            return False

        if not book["is_available"]:
            print(Messages.BOOK_ALREADY_LOANED.format(book["title"]))
            return False

        book["is_available"] = False
        book["current_holder"] = library_reader_role.lower()
        print(Messages.BOOK_LOANED.format(book["title"]))
        return True

    def return_book(self, book_identifier: str):
        book = self.find_book(book_identifier)

        if not book:
            print(Messages.BOOK_NOT_FOUND)
            return False

        if book["is_available"]:
            print(Messages.BOOK_ALREADY_AVAILABLE.format(book["title"]))
            return False

        book["is_available"] = True
        book["current_holder"] = None
        print(Messages.BOOK_RETURNED.format(book["title"]))
        return True

    def start_library(self):
        print("\nСИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
        book_add = "Добавить книгу"
        book_loan = "Выдать книгу"
        book_return = "Вернуть книгу"
        menu_enter = "Выход"
        first_menu_point = "1"
        second_menu_point = "2"
        third_menu_point = "3"
        fourth_menu_point = "4"

        library_reader_choice = None

        while library_reader_choice != fourth_menu_point:
            print("\nМЕНЮ:")
            print(f"{first_menu_point}. {book_add}")
            print(f"{second_menu_point}. {book_loan}")
            print(f"{third_menu_point}. {book_return}")
            print(f"{fourth_menu_point}. {menu_enter}")

            library_reader_choice = input(f"Выберите действие ({first_menu_point}-{fourth_menu_point}): ").strip()

            if library_reader_choice == first_menu_point:
                book_title = input("Название книги: ")
                book_author = input("Автор: ")

                published_book_year = None
                while published_book_year is None:
                    book_year_input = input("Год издания: ")
                    if book_year_input.isdigit():
                        published_book_year = int(book_year_input)
                    else:
                        print("Ошибка! Год издания должен быть числом. Попробуйте снова.")

                self.add_book_to_catalog(book_title, book_author, published_book_year)

            elif library_reader_choice == second_menu_point:
                book_id = input("ID книги или название: ")
                self.loan_book(book_id)

            elif library_reader_choice == third_menu_point:
                book_id = input("ID книги или название: ")
                self.return_book(book_id)

            elif library_reader_choice == fourth_menu_point:
                print("До свидания!")
            else:
                print("Неверный выбор. Попробуйте снова.")