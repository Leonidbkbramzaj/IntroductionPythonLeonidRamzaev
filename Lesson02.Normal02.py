## Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

import datetime

a = int(input("Input a year"))
b = int(input("Input a month"))
c = int(input("Input a day"))


time_simple = datetime.date(a, b, c).strftime("%d, %A.%B.%Y")

print(time_simple)

