elem = input().split()
lst = [[elem[0]]]
for i in range(1, len(elem)):
    if elem[i] == elem[i - 1]:
        lst[-1].append(elem[i])
    else:
        lst.append([elem[i]])

print(lst)