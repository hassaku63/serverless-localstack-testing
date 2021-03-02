import random


def random_status():
    return random.randint(0, 2)


def handler(event, contxt):
    return {
        'hello': 1,
        'state': random_status(),
    }
