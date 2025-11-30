phone_book = {
    "Иван": "+7-123-456-78-90",
    "Петр": "+7-987-654-32-10",
    "Мария": "+7-555-444-33-22"
}

while True:
    print("\n--- телефонная книга ---")
    print("1 - показать все контакты")
    print("2 - добавить контакт")
    print("3 - удалить контакт")
    print("4 - выйти")
    
    choice = input("выберите действие: ")
    
    if choice == '1':
        print("все контакты:")
        if phone_book:
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("телефонная книга пуста")
    
    elif choice == '2':
        name = input("введите имя: ")
        if name in phone_book:
            print("контакт с таким именем уже существует!")
        else:
            phone = input("введите номер телефона: ")
            phone_book[name] = phone
            print(f"контакт '{name}' добавлен")
    
    elif choice == '3':
        name = input("введите имя контакта для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print(f"контакт '{name}' удален")
        else:
            print("контакт не найден")
    
    elif choice == '4':
        print("выход из программы")
        exit()
    
    else:
        print("неверный выбор")