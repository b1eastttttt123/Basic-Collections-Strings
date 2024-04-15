alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

step = int(input("Шаг шифровки: "))
message = input("Введите сообщение: ").upper()
result = ""

for letter in message:

    place = alphabet.find(letter)
    new_place = place + step

    if letter in alphabet:
        result += alphabet[new_place]
    else:
        result += letter

print("Зашифрованное сообщение:", result)
