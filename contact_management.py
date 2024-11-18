
contacts = {}
while True:
    print("\nВыберите действие:")
    print("1. Добавить контакт")
    print("2. Просмотреть все контакты")
    print("3. Найти контакт")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выход")

    choice = input('Введите номер действия: ')

    if choice == '1':
        name = input('Введите имя: ')
        phone = input('Введите телефон: ')

        contacts[name] = phone
        print('Контакт добавлен.')
    elif choice == '2':
        if not contacts:
            print('Список контактов пуст.')
        else:
            print('Список контактов:')
            for name, phone in contacts.items():
                print(f'{name}: {phone}')
    elif choice == '3':
        name = input('Введите имя контакта: ')
        if name in contacts:
            print(f'контакт {name}: {contacts[name]}')
        else:
            print(f'Контакт {name} не найден.')
    elif choice == '4':
        name = input('Введите имя контакта: ')
        if name in contacts:
            new_phone = input('Введите новый телефон: ')
            contacts[name] = new_phone
            print(f'Контакт {name} изменен на {new_phone}.')
        else:
            print(f"Контакт {name} не найден")
    elif choice == '5':
        name = input('Введите имя контакта: ')
        if name in contacts:
            del contacts[name]
            print(f'Контакт {name} удален.')
        else:
            print(f"Контакт {name} не найден.")
    elif choice == '6':
        break
