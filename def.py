# Функция def, параметры функции, локальные переменные, основной блок

# def number(a,b):
#     if a > b:
#         print(a, "max")
#     elif a == b:
#         print(a, 'равно', b)
#     else:
#         print(b, 'max')
#
# x = 18
# y = 2
# number(x, y)

x = 50

def number(x):
    print("x равен", x)
    x = 2
    print("замена локального x на", x)
