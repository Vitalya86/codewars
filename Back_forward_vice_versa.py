
list_num = list(map(int, input().split()))
temp_ch = list_num[len(list_num) - 1]
del list_num[len(list_num) - 1]
list_num.insert(0, temp_ch)
print(*list_num)

