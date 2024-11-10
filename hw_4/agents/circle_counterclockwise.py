import random

circle_counterclockwise_last = None

def circle_counterclockwise(observation, configuration):
    """
    По очереди играет 0, 2, 1, 0 
    """
    global circle_counterclockwise_last
    if observation.step > 0:
        circle_counterclockwise_last = (circle_counterclockwise_last + 1) % 3
    else:
        circle_counterclockwise_last= random.randrange(0, configuration.signs)
    return circle_counterclockwise_last