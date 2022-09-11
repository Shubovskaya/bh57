# Реализовать бинарный поиск элемента в отсортированном списке.
# 	Дан список чисел, пользователь вводит число, необходимо реализовать поиск
# 	введенного пользователем числа в этом списке с помощью бинарного поиска

def bin_search(list, value):
    first = 0
    last = len(list)-1
    while first <= last:
        mid = (first + last) // 2
        if list[mid] == value:
            return mid
        elif list[mid] > value:
            last = mid - 1
        else:
            first = mid + 1
    return None
new_list = [2, 4, 6, 8, 9, 10, 12, 15, 20]
print(bin_search(new_list, int(input("Введите число: "))))




