# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.



def my_round(number, ndigits) -> float:
    x = int((number // 1))
    c = float((((number - x) * (10 ** ndigits)) // 1) / (10**ndigits))
    z = float((number - (x + c))*10**ndigits)
    s = ((1 /(10 ** ndigits)))


    return float((x + c) if z < 0.5 else x + c + s)


print(my_round(2.679882887, 4))



number = 2.679882887
ndigits = 4
x = int((number // 1))
c = float((((number - x) * (10 ** ndigits)) // 1) / (10**ndigits))
z = float((number - (x + c))*10**ndigits)
s = ((1 /(10 ** ndigits)))

print(x, c, s)
print(x + c + s)

# не понимаю откуда берется при сложении x, c, s 0.00000000004






