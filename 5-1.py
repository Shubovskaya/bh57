# Вывести первые N чисел кратные M и больше K
from collections import Counter

M: int = int(input("Введите число: "))
K: int = int(input("Введите число: "))
N: int = int(input("Введите число: "))
i = 1

while N:
    if K % M == 0:
       print(K)
       N -= 1
    K += 1










