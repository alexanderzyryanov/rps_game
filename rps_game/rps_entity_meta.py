from rps_graph import RPSGraph


class RPSEntityMeta(type):
    entity_graph = RPSGraph()

    def __prepare__(name, *bases, great, less):
        great = (e.__name__ for e in great)
        less = (e.__name__ for e in less)
        RPSEntityMeta.entity_graph.extend(name, great, less)

        return {}

    def __new__(cls, *args, **kwargs):

        return super(RPSEntityMeta, cls).__new__(cls, *args)
