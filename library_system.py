class LibrarySystem:
    def __init__(self):
        self.__books_catalog = []
        self.__books_counter = 0

    def add_book_to_catalog(self, book_title, book_author, publication_year):
        self.__books_counter += 1
        book_id = f"{self.__books_counter:04d}"

        new_book = {
            "book_id": book_id,
            "title": book_title.strip(),
            "author": book_author.strip(),
            "year": publication_year,
            "is_available": True,
            "current_holder": None
        }

        self.__books_catalog.append(new_book)
        print(f"Книга добавлена! ID: {book_id}")
        return book_id

    def find_book(self, book_identifier):
        for book in self.__books_catalog:
            if book["book_id"] == book_identifier or book["title"].lower() == book_identifier.lower():
                return book
        return None

    def loan_book(self, book_identifier):
        book = self.find_book(book_identifier)
        library_role = "Читатель"

        if not book:
            print("Ошибка! Книга не найдена.")
            return False

        if not book["is_available"]:
            print(f"Книга '{book['title']}' уже выдана.")
            return False

        book["is_available"] = False
        book["current_holder"] = library_role.lower()
        print(f"Книга '{book['title']}' выдана на руки!")
        return True

    def return_book(self, book_identifier):
        book = self.find_book(book_identifier)

        if not book:
            print("Ошибка! Книга не найдена.")
            return False

        if book["is_available"]:
            print(f"Книга '{book['title']}' и так в библиотеке.")
            return False

        book["is_available"] = True
        book["current_holder"] = None
        print(f"Книга '{book['title']}' возвращена!")
        return True

    def start_library_system(self):
        print("\nСИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ")
        book_add = "Добавить книгу"
        book_loan = "Выдать книгу"
        book_return = "Вернуть книгу"
        menu_enter = "Выход"
        first_menu_point = "1"
        second_menu_point = "2"
        third_menu_point = "3"
        fourth_menu_point = "4"


        while True:
            print("\nМЕНЮ:")
            print(f"{first_menu_point}. {book_add}")
            print(f"{second_menu_point}. {book_loan}")
            print(f"{third_menu_point}. {book_return}")
            print(f"{fourth_menu_point}. {menu_enter}")

            choice = input(f"Выберите действие ({first_menu_point}-{fourth_menu_point}): ").strip()

            if choice == first_menu_point:
                title = input("Название книги: ")
                author = input("Автор: ")
                current_year = 2026

                year_input = input("Год издания: ")
                try:
                    year = int(year_input)
                except ValueError:
                    year = current_year

                self.add_book_to_catalog(title, author, year)

            elif choice == second_menu_point:
                book_id = input("ID книги или название: ")
                self.loan_book(book_id)

            elif choice == third_menu_point:
                book_id = input("ID книги или название: ")
                self.return_book(book_id)

            elif choice == fourth_menu_point:
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
