from rps_game import RPSEntityRock

from rps_game import RPSEntityPaper

from rps_game import RPSEntityScissors

from rps_game import rps_game


if __name__ == '__main__':
    print(rps_game(RPSEntityPaper, RPSEntityRock))
    print(rps_game(RPSEntityRock, RPSEntityRock))
    print(rps_game(RPSEntityScissors, RPSEntityRock))

