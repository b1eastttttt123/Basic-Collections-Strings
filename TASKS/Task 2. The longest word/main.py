import math

text_user = input('Введите строку: ')

max_word = max(text_user.split(), key=len)

print(f"Самое длинное слово: «{max_word}».", f"Длина этого слова: {len(max_word)} символов.", sep="\n")

