def add_author_books(authors_books):
    author = input("Введите имя автора: ")
    books = input("Введите названия книг через запятую: ")

    book_list = [book.strip() for book in books.split(',')]
    # Добавляем книги к автору
    if author in authors_books:
        authors_books[author].extend(book_list)  # Если автор уже есть, добавляем книги к существующим
    else:
        authors_books[author] = book_list  # Если автора нет, создаем новую запись


def find_books(authors_books):
    author = input("Введите фамилию автора для поиска книг: ")
    if author in authors_books:
        print(f"Книги автора {author}:")
        for book in authors_books[author]:
            print(f'- "{book}"')
    else:
        print(f"Автор {author} не найден.")


biblioteka = {
    "Булгаков": ["Собачье сердце", "Мастер и Маргарита", "Белая гвардия"],
    "Пушкин": ["Евгений Онегин", "Капитанская дочка", "Дубровский"],
    "Кинг": ["Оно", "Сияние", "Кладбище домашних животных"],
    "Лавкрафт": ["Хребты безумия", "Зов ктулху", "Дагон"],
}

while True:
    print("\n1. Добавить книги для автора")
    print("2. Найти книги по автору")
    print("3. Выход")

    choice = input("Выберите действие (1-3): ")

    if choice == '1':
        add_author_books(biblioteka)
    elif choice == '2':
        find_books(biblioteka)
    elif choice == '3':
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
