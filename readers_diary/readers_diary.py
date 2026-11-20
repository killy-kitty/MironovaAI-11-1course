def show_menu():
    print("1 - добавить книгу")
    print("2 - показать все книги")
    print("3 - Последние 5 книг")
    print("4 - Изменить книгу")
    print("5 - Найти книгу")
    print("6 - Статистика")
    print("0 - Выход")

def add_book(books):
    name = input("Название книги: ").strip()
    if  name == "":
        print("Ошибка, нет названия")
    else:
        books.append(name)
        print("Книга добавлена")

def show_books(books):
    for book in books:
        print(book)

def last_five_books(books):
    for book in books[-5:]:
        print(book)

def edit_book(books):
    number = int(input("Номер книги: "))
    if 0 < number <= len(books):
        books[number - 1] = input("Новое название: ").strip()
        print("Книга изменена")
    else:
            print("Такой книги нет")

def find_book(books):
    word = input("Введите слово для поиска: ").lower()
    for book in books:
        if word in book.lower():
            print("Найденная книга: ", book)

def statistics(books):
    print("Всего книг: ", len(books))
    if len(books) > 0:
        print("Первая книга: ", books[0])
        print("Последняя книга: ", books[-1])

def main():
    print("----------------------------")
    print("=== ЧИТАТЕЛЬСКИЙ ДНЕВНИК ===")
    print("----------------------------")

books = []

while True:
    show_menu()
    point = input("выберите пункт: ")

    if point == "0":
        print("Выход")
        break  
    elif point == "1":
        add_book(books)
    elif point == "2":
        show_books(books)
    elif point == "3":
        last_five_books(books)
    elif point == "4":
        edit_book(books)
    elif point == "5":
        find_book(books)
    elif point == "6":
        statistics(books)
    else:
        print("Неверный пункт")
