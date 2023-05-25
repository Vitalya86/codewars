# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.


def increment_string(strng):
    if strng == '': # Если сторока пустая возвращаем str 1
        return '1'
    if strng.isalpha():
        return strng + '1' #  Если в строке нет цифр, то возвращаем строку и добавляем str 1
    else:
        num = ''
        alph = ''
        for i in strng[::-1]: # идем сконца списка и забирем все цифры как только встречается буква заканчиваем цикл. Т.к. по условию нам нужны только цифра в конце стройки, остальные не трогаем
            if i.isdigit():
                num += i
                s_l = len(num)
            else:
                break
        alph += strng[:-s_l] # Берем часть сторки без цифр
        n_num = int(num[::-1]) + 1 # переводим в int и добавляем + 1 не забываем перевернуть так как мы забирали цифры с обратном порядке
        return (f'{alph}{n_num:0{s_l}}') # Возвращяем результат и так как после веревода в int он убирает впереди 0 мы их добавляем если они нужны



print(increment_string('foo9'))