# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

elements = int(input("Input the number of elements: "))

random_list = []

for i in range(elements):
    random_list.append(random.randint(-100, 100))

print(random_list)