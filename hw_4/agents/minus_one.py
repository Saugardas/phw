import random

def minus_one(observation, configuration):
    """
    То, что проигрывало прошлому выбору соперника (+2)
    Был камень - возвращаем ножницы, была бумага - возвращаем камень
    """
    if observation.step > 0:
        return (observation.lastOpponentAction + 2) % 3
    else:
        return random.randrange(0, configuration.signs)