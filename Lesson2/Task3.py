# 3. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму.

print('Программа создаёт список из n чисел последовательности (1+1/n)^n и вычисляет их сумму.')
n = int(input('Введите число n: ')) 
num = [round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]
print(num)
print('Сумма чисел последовательности равна: ', round(sum(num), 3))