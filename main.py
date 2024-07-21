import re

from Classes.Library import Library

library = Library()
print('''
пример команд:
- Добавление_книги "Капитанская дочка" "Пушкин А.С." "1836"
- Отображение_всех_книг
- Удаление_книги 1 
- Поиск_книги "title" "Капитанская дочка"
- Изменить_статус_книги 2 "в наличии"
''')

while True:
    user_input = input("Введите команду: ").strip().split(maxsplit=1)

    if not user_input:
        print("Пустая команда. Пожалуйста, попробуйте еще раз.")
        continue

    command = user_input[0]
    args = user_input[1] if len(user_input) > 1 else ""
    if command == "Отображение_всех_книг":
        for key, value in library.get_all_books().items():
            print(f"ID: {key}")
            for i, j in value.items():
                print(f"{i}: {j}")

    elif command == "Добавление_книги":
        try:
            title, author, year = args.strip().split('" "')
            title = title.strip('"')
            author = author.strip('"')
            year = year.strip('"')
            print(library.added_book(title, author, year))
        except ValueError:
            print("Неверный формат команды. Используйте: Добавление_книги \"Название\" \"Автор\" \"Год\"")

    elif command == "Удаление_книги":
        try:
            print(library.delete_book(args.strip()))
        except ValueError:
            print("Неверный формат команды. Используйте: Удаление_книги ID")

    elif command == "Поиск_книги":
        try:
            search_key, search_value = args.strip().split('" "')
            search_key = search_key.strip('"')
            search_value = search_value.strip('"')
            search_criteria = {search_key: search_value}
            for item in library.search_book(search_criteria):
                for key, value in item.items():
                    print(f"ID: {key}")
                    for i, j in value.items():
                        print(f"{i}: {j}")
        except ValueError:
            print("Неверный формат команды. Используйте: Поиск_книги \"ключ\" \"значение\"")

    elif command == "Изменить_статус_книги":
        try:
            match = re.match(r'(\d+) "(.*)"', args)
            if match:
                book_id = match.group(1)
                status = match.group(2)
                print(library.change_status_book(book_id.strip(), status))
            else:
                print("Неверный формат команды. Используйте: Изменить_статус_книги ID \"статус\"")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Неизвестная или некорректная команда. Пожалуйста, попробуйте еще раз.")
