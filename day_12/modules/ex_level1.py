import random
import string


# 1.
def random_user_id(long=5):
    user_id = ''
    for _ in range(long + 1):
        random_alphanumeric = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        user_id += random_alphanumeric
    return user_id


# 2.
def user_id_gen_by_user():
    [a, b] = input('Ingrese largo y cantidad: ').split()
    for _ in range(int(b)):
        print(random_user_id(long=int(a)))


# 3.
def rgb_color_gen():
    def color():
        return random.randint(0, 255)
    return f'rgb({color()},{color()},{color()})'
