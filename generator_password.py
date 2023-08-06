import random, string


def gen_pass(len_pas):
    get_list = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = random.choices(get_list, k=len_pas)
    return ''.join(password)


len_pas = int(input('Укажите длину пароля(не менее 9 символов): '))

print(gen_pass(len_pas))
