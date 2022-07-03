import random

random_number = str(random.randint(1, 2))
user_number = input("Ввести число (от 1 до 2): ")

if user_number >= random_number:
    print("Супер!")
else:
    print("Нет!")
    print(f"Загаданное число {random_number}")