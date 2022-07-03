import random

random_number = str(random.randint(1, 2))
user_number = input("Угадай число (от 1 до 2): ")

if user_number == random_number:
    print("Вы угадали!")
else:
    print("Вы НЕ угадали!")
    print(f"Было загадано число: {random_number}")



