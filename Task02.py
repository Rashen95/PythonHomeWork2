# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число, а я выведу набор произведений чисел от 1 до введенного: '))
product_of_numbers = 1
list_of_numbers = []
for i in range(1, number+1):
    product_of_numbers *= i
    list_of_numbers.append(product_of_numbers)
print(list_of_numbers)
