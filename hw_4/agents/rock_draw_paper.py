from helpers.score_helper import get_score_last_game

rock_draw_paper_last = None

def rock_draw_paper(observation, configuration):
    """
    Если была ничья - бумага
    Иначе - всегда камень
    """
    global rock_draw_paper_last
    if observation.step > 0:
        if get_score_last_game(rock_draw_paper_last, observation.lastOpponentAction) == 0:
            rock_draw_paper_last = 1
        else:
            rock_draw_paper_last = 0
    else:
        rock_draw_paper_last = 0
    return rock_draw_paper_last