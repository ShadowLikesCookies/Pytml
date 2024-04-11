import string
import random

def generate_class_name(length):
    letters = string.ascii_lowercase
    class_name = ''.join(random.choice(letters) for _ in range(length))
    print(class_name)
    return class_name