from rps_game import RPSEntityMeta

from rps_game import RPSEntityRock

from rps_game import RPSEntityPaper

from rps_game import RPSEntityScissors


class RPSEntityWell(metaclass=RPSEntityMeta,
                    great=[RPSEntityRock, RPSEntityScissors],
                    less=[RPSEntityPaper]):
    pass


if __name__ == '__main__':
    print(RPSEntityMeta.rps_game(RPSEntityPaper, RPSEntityRock))
    print(RPSEntityMeta.rps_game(RPSEntityRock, RPSEntityRock))
    print(RPSEntityMeta.rps_game(RPSEntityScissors, RPSEntityRock))
    print(RPSEntityMeta.rps_game(RPSEntityWell, RPSEntityRock))

