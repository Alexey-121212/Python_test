# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

# Пример:

# n = 6 -> 1 4 1  
# n = 24 -> 4 16 4    
# n = 60 -> 10 40 10 

"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

n = 60

# Введите ваше решение ниже
print(int(n/6), int(n/6*4), int(n/6))