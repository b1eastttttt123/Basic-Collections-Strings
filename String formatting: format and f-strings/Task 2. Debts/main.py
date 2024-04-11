name_debtor = input("Введите имя должника: ")
dept = int(input(f"Введите долг, {name_debtor}: "))

message = "{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!".format(name_debtor, dept)

print(message)
