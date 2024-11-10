circle_pairs_list = [0, 0,1, 1, 2, 2]

def circle_pairs(observation, configuration):
    """
    По очереди отдаёт 0, 0, 1, 1, 2, 2, 0... 
    """
    global circle_pairs_list
    circle_pairs_list = circle_pairs_list[1:] + [circle_pairs_list[0]]
    return circle_pairs_list[-1]