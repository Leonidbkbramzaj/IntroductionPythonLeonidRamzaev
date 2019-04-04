# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


import math

a = int(input("введите коэффициент a:   "))
b = int(input("введите коэффициент b:   "))
c = int(input("введите коэффициент c:   "))

discriminant = (b ** 2) - 4 * a * c

print("значение дискриминанта =", discriminant)

if discriminant < 0:
    print("Уравнение не имеет решения")

elif discriminant == 0:
    x = (-1 * b / (2 * a))
    print("Один корень квадратного уровнения: ", x)

elif discriminant > 0:
    x = (((-1 * b) + math.sqrt(discriminant)) / (2 * a))
    y = (((-1 * b) - math.sqrt(discriminant)) / (2 * a))
    print("Первый корень квадратного уровнения: ", x)
    print("Второй корень квадратного уровнения: ", y)









