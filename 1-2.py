text: str = input("Введите текст: ")

d = {c:text.count(c) for c in text}
print(d)





