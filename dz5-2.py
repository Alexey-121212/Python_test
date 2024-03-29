# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.

# Пример использования На входе:


# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе:


# 19

arr = [5, 8, 6, 4, 9, 2, 7, 3]

# Введите ваше решение ниже

max = 0
if len(arr)>2:
    for i in range(1,len(arr)-1):
        if (arr[i]+arr[i+1]+arr[i-1])>max:
            max = arr[i]+arr[i+1]+arr[i-1]
else:
    for i in range(0,len(arr)):
        max+=arr[i]
        
print(max)