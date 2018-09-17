# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random

n = int(input('Введите число желаемое кол-во чисел: '))
#try:
     #n = n.isdigit()
#except:
    #input("Вы ввели не число")
i = 0
list_numbers = []
while i < n:
    numbers = int(random.random() * 100)
    list_numbers.append(numbers)
    i += 1

list_2 = [x ** 2 for x in list_numbers]

print('{} --> {}'.format(list_numbers, list_2))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
list_fruit_1 = input("Введите спимок фруктов, через запятую: ").split(',') #бананы,авокадо,груша,яблоко,мандарины
list_fruit_2 = input("Введите спимок фруктов, через запятую: ").split(',') #манго,киви,апельсины,мандарины

list_fruit_all = []

[list_fruit_all.append(x) for x in list_fruit_1 + list_fruit_2]
list_fruit_all = set(list_fruit_all)
print(list_fruit_all)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
n = int(input("Введите кол-во чисел: "))
i = 0
list_y = []
while i < n:
    x = random.randint(-1000, 1000)
    list_y.append(x)
    i += 1
print(list_y)

new_list_x = []
[new_list_x.append(x) for x in list_y if x > 0 and x % 3 == 0 and x % 4 != 0]
print('Найдено', len(new_list_x), 'элементов: ', new_list_x)
