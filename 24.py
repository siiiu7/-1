with open('tests.txt', mode='r') as test:
    a = test.readline().split()
count = 0
b = []
c = {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
     6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
d = {1: 'десять', 2: 'двадцать', 3: 'тридцать', 4: 'сорок',
     5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
     8: 'восемьдесят', 9: 'девяносто'}
e = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
     14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
     17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
f = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста',
     5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот',
     9: 'девятьсот'}
for i in range(len(a) - 1):
    if int(a[i + 1], 16) < int(a[i], 16) <= 1024:
        if count == 0:
            b.append(int(a[i], 16))
        count += 1
    else:
        count = 0
for i in b:
    g = len(str(i))
    for j in range(g):
        if g == 4:
            print('одна тысяча', end=' ')
            g -= 1
        elif g == 3:
            if int(str(i)[abs(g - len(str(i)))]) != 0:
                print(f[int(str(i)[abs(g - len(str(i)))])], end=' ')
            g -= 1
        elif g == 2:
            if int(str(i)[abs(g - len(str(i)))]) == 0:
                g -= 1
                print(c[int(str(i)[abs(g - len(str(i)))])])
                g -= 1
            elif str(i)[abs(g - len(str(i)))] != '1':
                print(d[int(str(i)[abs(g - len(str(i)))])], end=' ')
                g -= 1
                print(c[int(str(i)[abs(g - len(str(i)))])])
            else:
                print(e[int(str(i)[-2:])])
                g = 0
