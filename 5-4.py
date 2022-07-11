# Вводится строка. Определить кол-во пар одинаковых символов рядом стоящих в строке

text: str = input()
i = 0
c = 0

while i < len(text) - 1:
    if text[i] == text[i+1]:
        c += 1
        i += 1
    i += 1
print(c)