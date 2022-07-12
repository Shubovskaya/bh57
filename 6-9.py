# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

dict = {
    1: {
        "fname": "Misha",
         "lname": "Mihailov",
         "phone_number": +375291111111,
         "email": "mail@mail.ru"
},
    2: {
        "fname": "Misha",
         "lname": "Mihailov",
         "phone_number": +375291111111,
    },
    3: {
         "fname": "Rita",
         "lname": "Ivanova",
         "phone_number": +375299518521,
         "email": ""
    }}

for dict in dict.values():
    if not dict.get('email'):
        print(dict["fname"])




