# Создаем пустой словарь для хранения контактов
phone_book = {}

# Функция добавления контакта
def add_contact(name, phone):
    phone_book[name] = phone

    # Функция поиска номера по имени
def search_by_name(name):
    if name in phone_book:
        return phone_book[name]
    else:
        return "Кт не найден"

# Функция изменения контакта
def update_contact(name, phone):
    if name in phone_book:
        phone_book[name] = phone
        return "Контакт успешно изменен"
    else:
        return "Контакт не найден"

# Функция удаления контакта
def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        return "Контакт успешно удален"
    else:
        return "Контакт не найден"

# Основной цикл программы
while True:
    print("Выберите действие:")
    print("1 - добавить контакт")
    print("2 - найти номер по имени")
    print("3 - изменить контакт")
    print("4 - удалить контакт")
    print("5 - выход")

    choice = int(input("> "))

    if choice == 1:
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        add_contact(name, phone)
        print("Контакт успешно добавлен")

    elif choice == 2:
        name = input("Введите имя: ")
        result = search_by_name(name)
        print(result)

    elif choice == 3:
        name = input("Введите имя: ")
        
        if name in phone_book:
            new_phone = input("Введите новый номер телефона: ")
            update_contact(name, new_phone)
            print("Контакт успешно изменен")
        else:
            print("Контакт не найден")

    elif choice == 4:
        name = input("Введите имя: ")
        
        if name in phone_book:
            delete_contact(name)
            print("Контакт успешно удален")
        else:
            print("Контакт не найден")

    elif choice == 5:
        break

    else:
        print("Ты чёт не то вел")