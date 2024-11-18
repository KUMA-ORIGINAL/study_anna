import datetime

# text = input()
# n = int(input())
# for i in range(n):
#     print(text)

# a = input()
# total = 0
# for i in a:
#     total += int(i)
# print(total)

# number = input()
# flag = 'NO'
# valid_letters = 'АВЕКМНОРСТУХ'
#
# if 9 <= len(number) <= 10:
#     letters = number[0] + number[4:6]
#     digits = number[1:4] + number[7:]
#     under_space = number[6]
#
#     if digits.isdigit() and under_space == '_':
#         flag = 'YES'
#
#     for letter in letters:
#         if letter not in valid_letters:
#             flag = 'NO'
#             break
#
# print(flag)

# products = input().split(', ')
# product = input()
#
# if product in products:
#     print(f'{product} есть в списке покупок.')
# else:
#     print(f'{product} отсутствует в списке покупок.')

# numbers = []
# for i in range(1, 5):
#     for j in range(2):
#         numbers.append(i * j)
#
# numbers = [i * j for i in range(1, 5) for j in range(2)]
# print(numbers)


# n = int(input())
# students = [input().split() for i in range(n)]
# for i in students:
#     print(*i)
# print()
# for j in students:
#     if int(j[-1]) >= 4:
#         print(*j)

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# morse = dict(zip(letters, morse))
#
# text = input().upper()
# for i in text:
#     if i in morse:

# import random
#
# choices = ['камень', 'ножницы', 'бумага']
#
# while True:
#     user_choice = input('Введите (камень, ножницы, бумага): ')
#     bot_choice = random.choice(choices)
#     if bot_choice == user_choice:
#         result = 'Ничья!'
#     elif (bot_choice == 'камень' and user_choice == 'бумага' or
#           bot_choice == 'ножницы' and user_choice == 'камень' or
#           bot_choice == 'бумага' and
#           user_choice == 'ножницы'):
#         result = 'Победа'
#     else:
#         result = 'Поражение'
#     print(f'Результат: {result}\n'
#           f'Ваш выбор: {user_choice}\n'
#           f'Выбор компьютера: {bot_choice}')
#     play_again = input('хотите сыграть еще? (да/нет): ')
#     if play_again.lower() == 'нет':
#         print('До скорого!')
#         break

# contact = {}
# name = input()
# number = input()
# contact[name] = number
# print(f'{name} добавлен')
# print(contact)


# a = {
#    '345345': {
#        'number': 3453,
#        'time': 3453
#    },
# }
# a_number = input()
# if a[a_number]['paid']:
#     print('Number is present')

a = {
    11: {
        'car_number': 'sdf234',
        'time': datetime.datetime(2024, 11, 18, 18, 40),
        'paid': False
    }
}

start_time = datetime.datetime(2024, 11, 18, 18, 40)
end_time = datetime.datetime(2024, 11, 18, 20, 20)
difference = end_time - start_time
hours = difference.seconds // 3600
minutes = (difference.seconds % 3600) // 60
print(hours)
print(minutes)
