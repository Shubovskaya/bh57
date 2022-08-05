# # Пользователь вводит предложение, заменить все пробелы на "-" двумя способами
# text: str = input("enter some words: ") # Hello my dear friend
# print(text)
# print(text.replace(" ", "-")) # first method
# words = text.split("-")
# print(words)
# text = "-".join(words)
# print(text)()


import threading
from time import sleep
from datetime import datetime

def main():
    start_time = datetime.now()
    for i in range(1, 11):
        print(i)
        sleep(1)
    end_time = datetime.now()
    print(end_time-start_time)


if __name__== "__main__":
    threads = []
    for _ in range(10):
        threads.append(threading.Thread(target=main))
    for thread in threads:
        thread.start()