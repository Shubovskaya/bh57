# Пользователь вводит предложение, заменить все пробелы на "-" двумя способами
text: str = input("enter some words: ") # Hello my dear friend
print(text)
print(text.replace(" ", "-")) # first method
words = text.split("-")
print(words)
text = "-".join(words)
print(text)

