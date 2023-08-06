import random
random_num = random.randint(1, 100)
input_num = int(input('Введите целое число в диапазоне от 1 до 100: '))
while True:
    if input_num < random_num:
        input_num = int(input('Слишком мало, попробуйте еще раз: '))

    elif input_num > random_num:
        input_num = int(input('Слишком много, попробуйте еще раз: '))

    else:
        print(f'Вы угадали, поздравляем! {input_num} = {random_num}')
        break

