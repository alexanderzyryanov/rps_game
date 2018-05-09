from .rps_game import RPSGame

from .rps_entity_rock import RPSEntityRock

from .rps_entity_paper import RPSEntityPaper


class RPSEntityScissors(metaclass=RPSGame, great=[RPSEntityPaper], less=[RPSEntityRock]):
    pass
