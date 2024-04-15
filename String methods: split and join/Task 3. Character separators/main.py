while True:
    grats_template = input("Введите шаблон поздравления, "
                           "в шаблоне можно использовать конструкцию {name} и {age}: "
                           "С днём рождения, {name}! С {age}-летием тебя! ")
    if "{name}" in grats_template and "{age}" in grats_template:
        break
    print("Ошибка! Отсутствует одна или несколько конструкций!")

names_list = input("Введите список людей через запятую: ").split(",")
# если ввод только через запятую то пробел не добавялем, если с пробелом то - .split(", ")
ages_str = input("Введите возраст людей через пробел: ")
ages = [int(age) for age in ages_str.split()]

for i_man in range(len(names_list)):
    print(grats_template.format(name=names_list[i_man], age=ages[i_man]))

for index, name in enumerate(names_list):
    print(grats_template.format(name=name, age=ages[index]))

# Вариант с небольшой долей "магии" (инструмент будет изучен в будущих модулях):
for age, name in zip(ages, names_list):  # zip соединяет списки и можно брать сразу по элементу из каждого
    print(grats_template.format(name=name, age=age))

people = [" ".join([names_list[index], str(ages[index])]) for index in range(len(names_list))]
print("Именинники:", ", ".join(people))
