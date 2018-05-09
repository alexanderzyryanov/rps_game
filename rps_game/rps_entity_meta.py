from rps_graph import RPSGraph


class RPSEntityMeta(type):
    _entity_graph = RPSGraph()

    @classmethod
    def __prepare__(mcs, name, *bases, great, less):
        great = (e.__name__ for e in great)
        less = (e.__name__ for e in less)
        mcs._entity_graph.extend(name, great, less)

        return {}

    def __new__(mcs, *args, **kwargs):

        return super(RPSEntityMeta, mcs).__new__(mcs, *args)

    @classmethod
    def rps_game(mcs, left, right):
        if type(left) is not RPSEntityMeta:
            raise ValueError()

        if type(right) is not RPSEntityMeta:
            raise ValueError()

        if left is right:
            return 0

        left = left.__name__
        right = right.__name__
        if right in mcs._entity_graph[left]:
            return 1

        return -1
