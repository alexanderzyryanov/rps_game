from .rps_entity_meta import RPSEntityMeta


def rps_game(left, right):
    if type(left) is not RPSEntityMeta:
        raise ValueError()

    if type(right) is not RPSEntityMeta:
        raise ValueError()

    if left is right:
        return 0

    left = left.__name__
    right = right.__name__
    if right in RPSEntityMeta.entity_graph[left]:
        return 1

    return -1
