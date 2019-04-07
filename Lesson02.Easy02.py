# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

rate = [2, 5, 6, 7, 4, 9]
index = [5, 6, 8, 9, 12]


crosslist = set(rate).intersection(index)

print(crosslist)

print("deleting elements....")

print("the elements,", str(crosslist),  "have been deleted")

for i in rate[:]:
    if i in index:
     rate.remove(i)
print(rate)





