from .rps_entity_meta import RPSEntityMeta

from .rps_entity_rock import RPSEntityRock


class RPSEntityPaper(metaclass=RPSEntityMeta, great=[RPSEntityRock], less=[]):
    pass
