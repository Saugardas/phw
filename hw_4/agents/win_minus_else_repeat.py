import random
from helpers.score_helper import get_score_last_game

win_minus_else_repeat_last = None

def win_minus_else_repeat(observation, configuration):
    """
    Если прошлая игра была выигрышная - меняем ход -1 (ходим как соперник)
    Иначе - повторяем ход
    """
    global win_minus_else_repeat_last
    if observation.step > 0:
        if get_score_last_game(win_minus_else_repeat_last, observation.lastOpponentAction) == 1:
            win_minus_else_repeat_last = (win_minus_else_repeat_last + 1) % 3
        else:
            return win_minus_else_repeat_last
    else:
        win_minus_else_repeat_last = random.randrange(0, configuration.signs)
    return win_minus_else_repeat_last