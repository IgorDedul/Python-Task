# Задача №2: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Программа, которая составит список простых множителей числа N.")
num = int(input("Введите число: "))
i = 2 # первое простое число
list = []
old = num
while i <= num:
    if num % i == 0:
        list.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простыми множителями числа {old} являются: {list}")