import random
from helpers.score_helper import get_score_last_game

repeat_win_else_plus_last = None

def repeat_win_else_plus(observation, configuration):
    """
    Если прошлая игра была выигрышная - повторяем ход
    Иначе - возвращаем то, что победило бы соперника в прошлой игре
    """
    global repeat_win_else_plus_last
    if observation.step > 0:
        if get_score_last_game(repeat_win_else_plus_last, observation.lastOpponentAction) == 1:
            return repeat_win_else_plus_last
        else:
            repeat_win_else_plus_last = (repeat_win_else_plus_last + 1) % 3
    else:
        repeat_win_else_plus_last = random.randrange(0, configuration.signs)
    return repeat_win_else_plus_last