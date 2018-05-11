from .rps_game import RPSGame

from .rps_entity_rock import RPSEntityRock


class RPSEntityPaper(metaclass=RPSGame):
    great = (RPSEntityRock, )
    less = ()
