import random
from colorama import init


init()
from colorama import Fore, Back, Style
print(Fore.MAGENTA)

#random_number = str(random.randint(1, 2))
#user_number = input("Угадай число (от 1 до 2): ")

#if user_number == random_number:
    #print("Вы угадали!")
#else:
    #print("Вы НЕ угадали!")
   # print(f"Было загадано число: {random_number}")

M: int = int(input("Введите число: "))
K: int = int(input("Введите число: "))
N: int = int(input("Введите число: "))
i = 1

while N:
    if K % M == 0:
       print(K)
       N -= 1
    K += 1












