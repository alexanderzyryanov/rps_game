from .rps_entity_meta import RPSEntityMeta

from .rps_entity_rock import RPSEntityRock

from .rps_entity_paper import RPSEntityPaper


class RPSEntityScissors(metaclass=RPSEntityMeta, great=[RPSEntityPaper], less=[RPSEntityRock]):
    pass
