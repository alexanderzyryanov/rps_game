from .rps_entity_meta import RPSEntityMeta


def rps_game(left, right):
    if left is right:
        return 0

    left = left.__name__
    right = right.__name__
    if right in RPSEntityMeta.entity_graph._graph[left]:
        return 1

    return -1
