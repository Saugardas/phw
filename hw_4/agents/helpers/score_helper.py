def get_score_last_game(agent_action, opponent_action):
    if agent_action == opponent_action:
        res = 0
    elif ((agent_action + 1) % 3) == opponent_action:
        res = -1
    else:
        res = 1
    return res