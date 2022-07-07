# Вывести первые N чисел кратные M и больше K
from collections import Counter

M: int = int(input("Введите число: "))
K: int = int(input("Введите число: "))
N: int = int(input("Введите число: "))

for i in range(1, 101):
    if i % M == 0 and i > K:
        print(i)












