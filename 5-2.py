# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

a = float(input("Введите первое число: "))
operation = input("Введите действие: (+,-,*,/): ")
b = float(input("Введите второе число: "))
result = 0

if operation == "+":
    result = a+b
elif operation == "-":
    result = a-b
elif operation == "*":
    result = a*b
elif operation == "/":
    result = a/b
else:
    result = None
print(f"Результат: {result}")

