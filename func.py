# x = 50


# def number():
#     global x
#
#     print("x равен", x)
#     x = 2
#     print("Заменяем глобальное значение x на", x)
#
# number()
# print('Значение x составляет', x)

# def func_outer():
#     x = 2
#     print("x равно", x)
#
#     def func_inner():
#         x = 5
#
#     func_inner()
#     print("Локальное x сменилось на", x)
#
# func_outer()

# Значение аргументов по умолчанию

def say(message, times = 2):
    print(message * times)

say("Hello")
say("World" * 5)