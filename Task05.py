# Задание 5 Реализуйте алгоритм перемешивания списка.

amount_of_numbers = int(input('Сколько чисел будет в вашем списке: '))
numbers = []
for i in range(amount_of_numbers):
    numbers.append(i+1)
print(numbers)
print('А теперь я перемешаю твой список')
for i in range(round(amount_of_numbers/2)):
    if i % 2 == 0:
        numbers[i], numbers[len(numbers)-i-1] = numbers[len(numbers)-i-1], numbers[i]
    else:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers)
