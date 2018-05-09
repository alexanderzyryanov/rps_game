from rps_game import RPSGame

from rps_game import RPSEntityRock

from rps_game import RPSEntityPaper

from rps_game import RPSEntityScissors


class RPSEntityWell(metaclass=RPSGame,
                    great=[RPSEntityRock, RPSEntityScissors],
                    less=[RPSEntityPaper]):
    pass


if __name__ == '__main__':
    print(RPSGame.rps_game(RPSEntityPaper, RPSEntityRock))
    print(RPSGame.rps_game(RPSEntityRock, RPSEntityRock))
    print(RPSGame.rps_game(RPSEntityScissors, RPSEntityRock))
    print(RPSGame.rps_game(RPSEntityWell, RPSEntityRock))

