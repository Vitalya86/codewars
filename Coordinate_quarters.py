k = int(input('Введите колличество точек: '))
chI = 0
chII = 0
chIII = 0
chIV = 0

for _ in range(k):
    s = input().split()
    if int(s[0]) > 0:
        if int(s[1]) > 0:
            chI += 1
        elif int(s[1]) < 0:
            chIV += 1
    elif int(s[0]) < 0:
        if int(s[1]) > 0:
            chII += 1
        elif int(s[0]) < 0:
            if int(s[1]) < 0:
                chIII += 1
print(f'Первая четверть: {chI}')
print(f'Вторая четверть: {chII}')
print(f'Третья четверть: {chIII}')
print(f'Четвертая четверть: {chIV}')
