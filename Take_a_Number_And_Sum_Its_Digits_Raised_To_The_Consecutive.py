# version one
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for num in range(a, b + 1):
        summa = 0

        for i in range(len(str(num))):
            summa += int(str(num)[i]) ** (i + 1)

        if summa == num:
            result.append(num)
    return result


# version two

def sum_dig_pow(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]