n, m = int(input()), int(input())

matrix = []
for i in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)
st1, st2 = map(int, input().split())
for i in range(n):
    matrix[i][st1], matrix[i][st2] = matrix[i][st2], matrix[i][st1]
[print(*i) for i in matrix]