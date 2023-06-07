def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


total_lst = [list(map(int, input().split())) for _ in range(int(input()))]
count = 0
result = []
while count < len(total_lst):
    result = quick_merge(result, total_lst[count])
    count += 1
print(*result)

