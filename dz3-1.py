# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:

# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

# Пример использования На входе:

# coins = [0, 1, 0, 1, 1, 0]

# На выходе:

# 3
coins = [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
chet = 0
nechet = 0

# Введите ваше решение ниже
i=0
while i < len(coins) :
    if coins[i] == 0:
        chet+=1
    else:
        nechet+=1
    i+=1
if chet>nechet :
    print (nechet)
else:
    print (chet)