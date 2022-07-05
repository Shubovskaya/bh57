# Заполнить список степенями числа 2 (от 2^1 до 2^n).
n = int(input("Введите число: "))

a = [x ** 2 for x in range(int(n))]
print(a)








