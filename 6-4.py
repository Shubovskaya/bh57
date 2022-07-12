# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

text = [15, 1, 3, "Hello", 13, False, 5, "World", None, ","]
new_text = []

for i in text:
    if isinstance(i, str):
        new_text.append(i)
print(new_text)





