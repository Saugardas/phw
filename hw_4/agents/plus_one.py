import random

def plus_one(observation, configuration):
    """
    То, что побеждало прошлый выбор соперника (+1)
    Был камень - возвращаем бумагу, была бумага - возвращаем ножницы
    """
    if observation.step > 0:
        return (observation.lastOpponentAction + 1) % 3
    else:
        return random.randrange(0, configuration.signs)