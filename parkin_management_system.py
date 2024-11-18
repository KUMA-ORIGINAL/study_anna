import datetime

TARIFF_FIRST_HOUR = 100
TARIFF_NEXT_HOURS = 50

tickets = {
    0: {
        'car_num': 'ABC123',
        'issue_time': datetime.datetime(2024, 11, 18, 0, 30),
        'paid': False
    },
    1: {
        'car_num': 'XYZ456',
        'issue_time': datetime.datetime(2024, 11, 18, 9, 0),
        'paid': False
    },
    2: {
        'car_num': 'LMN789',
        'issue_time': datetime.datetime(2024, 11, 18, 9, 15),
        'paid': False
    }
}
count = 0

while True:
    print('\nВыберите действие:')
    print('1. Выдача талона')
    print('2. Сдача талона')
    choice = int(input('Ваш выбор: '))

    if choice == 1:
        car_num = input('Введите номер машины:')

        if not car_num.isalnum():
            print('Ошибка: Неверный формат номера машины. Пожалуйста, '
                  'введите номер в правильном формате (например, ABC123).')
            continue

        issue_time = datetime.datetime.now()
        tickets[count] = {
            'car_num': car_num,
            'issue_time': issue_time,
            'paid': False
        }
        print('Талон выдан:')
        print(f'Номер талона: {count}')
        print(f'Номер машины: {car_num}')
        print(f'Время выдачи: {issue_time}')

        count += 1
    elif choice == 2:
        ticket_num = int(input('Введите номер талона: '))

        if ticket_num not in tickets:
            print(f'Ошибка: Талон с номером {ticket_num} не найден. '
                  f'Пожалуйста, проверь те номер и попробуйте снова.')
            continue
        if tickets[ticket_num]['paid']:
            print(f'Ошибка: Талон с номером {ticket_num} уже оплачен. Въезд был ранее оплачен, '
                  f'необходимо обратиться к администратору парковки.')
            continue

        car_num = tickets[ticket_num]['car_num']
        issue_time = tickets[ticket_num]['issue_time']
        exit_time = datetime.datetime.now()

        parking_fee = 0
        difference_time = exit_time - issue_time
        hours = difference_time.seconds / 3600
        minutes = difference_time.seconds % 3600 // 60
        if hours < 1:
            parking_fee = int(hours * TARIFF_FIRST_HOUR)
        else:
            parking_fee = int(TARIFF_FIRST_HOUR + (hours - 1) * TARIFF_NEXT_HOURS)

        print(f'Номер талона: {ticket_num}')
        print(f'Номер машины: {car_num}')
        print(f'Время въезда: {issue_time}')
        print(f'Время выезда: {exit_time}')
        print(f'Продолжительность парковки: {int(hours)} часа {minutes} минут')
        print(f'Стоимость парковки: {parking_fee} сом')

        tickets[ticket_num]['paid'] = True
