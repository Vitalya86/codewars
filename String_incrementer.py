# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# version one
def increment_string(strng):
    if strng == '':
        return '1'
    if strng.isalpha():
        return strng + '1'
    else:
        num = ''
        alph = ''
        for i in strng[::-1]:
            if i.isdigit():
                num += i
                s_l = len(num)
            else:
                break
        alph += strng[:-s_l]
        n_num = int(num[::-1]) + 1
        return (f'{alph}{n_num:0{s_l}}')


# version two
def increment_string(str_):
    s = str_.rstrip('0123456789')
    n = str_[len(s):]
    return s + str(int(n) + 1).zfill(len(n)) if n else str_ + "1"