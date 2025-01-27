import random


def draw(undrawned: list, with_number = False) -> list:
    length = len(undrawned)
    drawned = []
    for i in range(length):
        item = random.choice(undrawned)
        if with_number: item.number = i + 1
        drawned.append(item)
        undrawned.remove(item)
    return drawned