# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# Пример

# На входе:


# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе:


# 3 5

var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

# Введите ваше решение ниже

list_1 = var1.split(' ')
list_1 = [int(elt) for elt in list_1]

list_2 = var2.split(' ')
list_2 = [int(elt) for elt in list_2]

list_3 = var3.split(' ')
list_3 = [int(elt) for elt in list_3]


list_fin = []

for i in range(0, list_1[0]):
    if (list_2[i] in list_3) & (list_2[i] not in list_fin):
        list_fin.append(list_2[i])
list_fin.sort()


print (*list_fin)


