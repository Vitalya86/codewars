n = int(input())
triangle = [[1]]
for i in range(1, n + 1):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)

print(triangle[-1])