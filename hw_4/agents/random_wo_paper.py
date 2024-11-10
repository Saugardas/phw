import random

def random_wo_paper(observation, configuration):
    """
    Всегда возвращаем случайное значение но без бумаги
    """
    return random.choice([0, 2])