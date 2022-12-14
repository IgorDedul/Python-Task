# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('Программа вычисляет сумму элементов списка, стоящих на нечётной позиции.')

size = int(input('Какое количество элементов вы хотите добавить список? Укажите число или поставьте 0 если хотите использовать заданный список: '))

if size == 0:
    list = [2, 3, 5, 9, 3]
elif size > 0:
    list = []
    for i in range (1, size + 1):
        list.append(int(input(f'Задайте {i} элемент: ')))
else: print('Ошибка ввода.')

print('Заданный список', list)

sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
print(f"Сумма равна: {sum}")