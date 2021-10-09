import random
import string


# 1.
def list_of_hexa_colors(q=3):
    list_hexa = []

    def random_hexa():
        hexa = '#'
        for _ in range(6):
            random_alphanumeric = random.choice('abcdef' + string.digits)
            hexa += random_alphanumeric
        return hexa

    for _ in range(q):
        list_hexa.append(random_hexa())

    return list_hexa


# 2.
def list_of_rgb_colors(q=3):
    list_rgb = []

    def color():
        return random.randint(0, 255)

    for _ in range(q):
        list_rgb.append(f'rgb({color()},{color()},{color()})')

    return list_rgb


# 3.
def generate_colors(type_color, q):
    if type_color == "hexa":
        print(list_of_hexa_colors(q=q))
    if type_color == "rgb":
        print(list_of_rgb_colors(q=q))


generate_colors('hexa', 3)  # ['#a3e12f','#03ed55','#eb3d2b']
generate_colors('hexa', 1)  # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
