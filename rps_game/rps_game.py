from rps_graph import RPSGraph


class RPSGame(type):
    _entity_graph = RPSGraph()

    def __new__(mcs, *args, **kwargs):
        name, _bases, cls_dict, *rest = args

        try:
            less = cls_dict['less']
        except KeyError:
            raise TypeError()

        try:
            great = cls_dict['great']
        except KeyError:
            raise KeyError()

        great = (e.__name__ for e in great)
        less = (e.__name__ for e in less)
        mcs._entity_graph.extend(name, great, less)

        return super(RPSGame, mcs).__new__(mcs, *args)

    @classmethod
    def rps_game(mcs, left, right):
        if type(left) is not RPSGame:
            raise ValueError()

        if type(right) is not RPSGame:
            raise ValueError()

        if left is right:
            return 0

        left = left.__name__
        right = right.__name__
        if right in mcs._entity_graph[left]:
            return 1

        return -1
