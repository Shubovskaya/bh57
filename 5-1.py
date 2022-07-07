# Вывести первые N чисел кратные M и больше K

N: int = int(input("Введите число: "))
M: int = int(input("Введите число: "))
K: int = int(input("Введите число: "))

for i in range(0, N, M):
    if i > K:
        print(i)



