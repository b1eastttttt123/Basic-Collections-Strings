name_user = input(f"Введите имя: ")
number_order = int(input("Введите номер заказа: "))

message = "\nЗдравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!".format(name_user, number_order)

print(message)

