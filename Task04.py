# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

N = int(input('Введите количество чисел, которое будет в массиве: '))
list_of_numbers = []
for i in range(N):
    list_of_numbers.append(-N+2*i)
print(list_of_numbers)
while True:
    a = int(input('Какой элемент по счету мне вывести первым: '))
    if 0 < a <= N:
        break
    else:
        print(f'Элемента с порядковым номером {a} нет')
while True:
    b = int(input('Какой элемент по счету мне вывести вторым: '))
    if 0 < b <= N:
        break
    else:
        print(f'Элемента с порядковым номером {b} нет')
print(list_of_numbers[a-1])
print(list_of_numbers[b-1])
