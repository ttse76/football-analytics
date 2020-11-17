import Utils.StatsUtil as util
import pandas as pd
import sys
import Models

YEAR = 2020
WEEKS = 10
AWAY_TEAM = 'PHI'
HOME_TEAM = 'CLE'

def set_options():
    util.set_year(YEAR)
    util.set_weeks(16)

def out(res):
    print('Number of games simulated: ' + str(res['num_games']))
    print('Weeks: ' + str(WEEKS) + '\n')
    print(AWAY_TEAM + ' win: ' + str(res['away']) + '%')
    print(HOME_TEAM + ' win: ' + str(res['home']) + '%')
    print('Tie: ' + str(res['tie']) + '%')

if __name__ == '__main__':
    set_options()
    home_team_info = util.getSeason(HOME_TEAM)
    away_team_info = util.getSeason(AWAY_TEAM)

    res = Models.modelA(away_team_info, home_team_info)
    out(res)


