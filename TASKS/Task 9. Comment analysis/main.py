def count_uppercase_lowercase(text):
    uppercase = 0
    lowercase = 0
    for letter in text:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1
    return uppercase, lowercase

text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
