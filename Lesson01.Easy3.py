
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет")

age = int (input("How old are you: "))

if age >= 18:
    print("Welcome to the party!")
else:
    print("You shall not pass!")


