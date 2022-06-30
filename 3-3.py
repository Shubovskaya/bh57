# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
name: str = "Alice"
age: str = 41
city: str = "Minsk"
text = "Hello. My name is %s. I`m %d years old. I live in %s" % (name, age, city)
print(text) # first method
text = "Hello. My name is {}. I`m {} years old. I live in {}".format(name, age, city)
print(text) # second method
text = f"Hello. My name is {name}. I`m {age} years old. I live in {city}"
print(text)
