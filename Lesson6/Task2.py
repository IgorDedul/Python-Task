# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

import math
print('Данная программа счмтает факториал указанного вами числа.')
n = int(input('Введите число, факториал которого будет посчитан: '))
print("Ваш результат: ", [math.factorial(i) for i in range (1,n+1)])