from random import randint
from random import randrange


class TestMethods:
    @staticmethod
    def get_random_string(lenght):
        return "".join(chr(randint(65, 90)) for _ in range(lenght))

    @staticmethod
    def get_random_numbers(max_number):
        return randrange(max_number)
