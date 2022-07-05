"""Заполнить словарь, где ключами будут выступать числа от 0 до n, а
значениями вложенный словарь с ключами "name" и "email", а значения
для этих ключей будут браться с клавиатуры
"""

key = int(input("Введите имя: "))
name: str = input("Введите имя: ")
email: str = input("Введите email: ")

d = {
    key : {
        name : email
    }
}
d = ({key:{name:email} for key in d})
print(d)


