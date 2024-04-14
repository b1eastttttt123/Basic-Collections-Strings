def findWord():
    user_text_list, text_list = [input(f"Введите {num + 1} слово: ") for num in range(3)], input("Введите любой текст: ")

    for word in user_text_list:
        print(f"Слово {word} встречается в тексте {text_list.count(word)} раз")

findWord()
