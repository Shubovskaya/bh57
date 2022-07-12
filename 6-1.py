# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def binary(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s
n = 10
print(str(binary))

# while 1:
#     n = int(input())
#     if n != 0:
#         print(binary(n))
#     else:
#         break





