lst_num = list(map(int, input().split()))


# result = 0
# for i in range(len(lst_num) - 1):
#     if lst_num[i] < lst_num[i + 1]:
#         result += 1
# print(result)

def more_previous(lst):
    return sum(1 for i in range(len(lst) - 1) if lst[i] < lst[i + 1])


print(more_previous(lst_num))

