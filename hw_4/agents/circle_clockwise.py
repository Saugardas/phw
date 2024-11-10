import random

circle_clockwise_last = None

def circle_clockwise(observation, configuration):
    """
    По очереди играет 0, 1, 2 
    """
    global circle_clockwise_last
    if observation.step > 0:
        circle_clockwise_last = (circle_clockwise_last + 1) % 3
    else:
        circle_clockwise_last= random.randrange(0, configuration.signs)
    return circle_clockwise_last