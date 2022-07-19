# Вывести в порядке возрастания цифры, входящие в десятичную запись натурального числа N.

N = int(input("Введите число: "))

def numbers_in_order(N):
    all_numbers = str(N)
    all_numbers = ",".join(sorted(all_numbers))
    return all_numbers
print(numbers_in_order(N))