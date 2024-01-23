
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:


# sum(2, 2)
# # 4

def sum(a,b):
    if (a==0) & (b==0):
        return 0
    if (a==0) & (b!=0):
        if b<0:
            return 1-sum(0,b-1)    
        else:
            return 1+sum(0,b-1)
    if (a!=0) & (b==0):
        return 1+sum(a-1,0)
    if b<0:
        return sum(a-1,b+1) 
    return 2+sum(a-1,b-1) 

# def sum(a,b):
#     res = 0
#     for i in range(0,a):
#         res = res+1
#     for i in range(0,b):
#         res = res+1
#     return res


print ("sum ", sum(10,-8))
