# import random
#
# random_number = random.randint(1, 5)
# user_number = input("Угадай число от 1 до 5: ")
#
# if user_number == random_number:
#     print("Вы угадали!")
# else:
#     print("Вы не угадали!")
# print(f"Было загадано число {random_number}")

some_digit = 12345

def sum(some_numbers):
    numbers = len(str(some_numbers))
    result = 0
    for num in range(numbers):
        result += int(str(some_digit[num]))
    return result

print(sum(some_digit))





