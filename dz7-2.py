# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# Пример

# На входе:


stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:


# Парам пам-пам
def rhythm(str):   
        phrase = str.split()
        list_1 = []
        for word in phrase:
        # word=word.split("-")
            vowels = 0
            for i in word:
                if i in 'аеёиоуыэюя':
                 vowels += 1
            list_1.append(vowels)
        return len(list_1) == list_1.count(list_1[0])

if " " not in stroka:
    print("Количество фраз должно быть больше одной!")
else:
    if rhythm(stroka):
        print('Парам пам-пам')
    else:
        print('Пам парам')