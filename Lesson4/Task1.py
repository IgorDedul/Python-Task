# 1. Вычислить число pi c заданной точностью d
#Пример: при d = 0.001,  pi = 3.141. 10^(-1) <= d10 <= 10^(-10)

print('Программа вычисляет число pi c заданной точностью')
rate = int(input('Введите число, с указанием точности, количество знаков после запятой: '))

import math
from math import pi
standard = pi

# Формула Бэйли — Боруэйна — Плаффа
n = rate
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# Ряд Лейбница
#def Leybins_pi(eps=10^(-rate)):
#    s=0
#    d=1
#    sgn=1
#    while True:
#        a=4/d
#        s=s+sgn*a
#        if a<eps:
#            return s
#        sgn=-sgn
#        d=d+2
  
print(f"Эталонное число Пи из функции: {standard}; число Пи по формуле Бэйли — Боруэйна — Плаффа: {my_pi}")

#print("Число Пи из расчёта ряда Лейбница: ", Leybins_pi())