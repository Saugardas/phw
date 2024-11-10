import random
from helpers.score_helper import get_score_last_game

win_random_else_repeat_last = None

def win_random_else_repeat(observation, configuration):
    """
    Если прошлая игра была выигрышная - ходим случайно
    Иначе - повторяем ход
    """
    global win_random_else_repeat_last
    if observation.step > 0:
        if get_score_last_game(win_random_else_repeat_last, observation.lastOpponentAction) == 1:
            win_random_else_repeat_last = random.randrange(0, configuration.signs)
        else:
            pass
    else:
        win_random_else_repeat_last = random.randrange(0, configuration.signs)
    return win_random_else_repeat_last