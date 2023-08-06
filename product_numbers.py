s = [int(input()) for _ in range(int(input()))]
k = int(input())
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] * s[j] == k:
            exit(print('ДА'))
print('НЕТ')
