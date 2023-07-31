# Stepik 4.5 'Магический квадрат'

n = int(input())

matrix = []
for _ in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)
digits = [i for i in range(1, n**2 + 1)]

d1, d2 = 0, 0
for i in range(n):
    stolb_sum, stroka_sum = 0, 0
    for j in range(n):
        stolb_sum += matrix[j][i]
        stroka_sum += matrix[i][j]
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    d1 += matrix[i][i]
    d2 += matrix[i][n - i - 1]
    if stolb_sum != stroka_sum:
        break

if stolb_sum == stroka_sum == d1 == d2 and digits == []:
    print('YES')
else:
    print('NO')