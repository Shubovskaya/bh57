# Дан список чисел, в которым числа погут повторяться подряд несколько раз,
# необходимо реализовать алгоритм сжатия данного списка следующим образом:
# 	Пример: [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 1]
# 	Результат: [1, 5, 2, 8, 3, 2, 4, 2, 5, 1, 1, 1]
# 	Пояснение: В результирующем списке на нечетных идексах идут числа из cписка, а на
# 	четных индексах, сколько раз подряд встретилось это число

# list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 1]
# new_list = []
#
# for i in range(list):
#     if i % 2 == 0:
#         i = list.count(1)
#         new_list.append(i)
#     else:
#         new_list.append(i)
# print(new_list)

# def get_hidden_card():
#     number = '2034399002125581'
#     star = 4
#     return "*" * star + number[12:]
# print(get_hidden_card())

# def get_hidden_card(number, star = 4):
#     number = '2034399002125581'
#     return "*" * star + number[12:]
#
# print(get_hidden_card("2034399002125581"))

# def trim_and_repeat(text="Hello, Python!", offset=7, repetitions=3):
#     return text[offset:] * repetitions
# print(trim_and_repeat())

# def get_age_difference(year_one, year_two):
#    difference = abs(year_one - year_two)
#    return f"The age difference is {difference}"
# print(get_age_difference(2007, 2013))

# from datetime import datetime
#
# date = datetime.now().timestamp()
# print(date)
# print(datetime.fromtimestamp(1658845466.965557))

# def has_upper_case(string):
#     upper_case = string.lower()
#     return upper_case == string.upper()
# print(has_upper_case("Hexlet"))

# def is_first_letter_an_a(string):
#     first_letter = string[0]
#     return first_letter == 'a'
#
# print(is_first_letter_an_a('orange'))

# def is_leap_year(year):
#     leap_year = year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)
#     return leap_year
# print(is_leap_year(2017))

# def string_or_not(string):
#     return isinstance(string, str) and "yes" or "no"
# print(string_or_not(698))