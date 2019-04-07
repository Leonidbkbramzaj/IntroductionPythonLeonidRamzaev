
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

#1

fruits = ["яблоко", "банан", "киви", "арбуз", "Дыня"]

print("1. {0:>10}".format(*fruits))
print("2. {1:>10}".format(*fruits))
print("3. {2:>10}".format(*fruits))
print("4. {3:>10}".format(*fruits))

number = 0

#2
for i in fruits:
    item_fruit = ("{0:>10}".format(i))
    number = number + 1
    print(str(number)+".", item_fruit)

# The first part of the code is for understanding the format functon
# The second part of the code is the solution prepared usinf for loop
