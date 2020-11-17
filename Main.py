import StatsUtil as util
import pandas as pd
import sys

YEAR = 2020
WEEKS = 16
AWAY_TEAM = ''
HOME_TEAM = 'CLE'

def set_options():
    util.set_year(YEAR)
    util.set_weeks(16)

if __name__ == '__main__':
    set_options()
    team_info = util.getSeason(HOME_TEAM)
    scores = util.getScoreStats(team_info)
    for x in scores:
        print(x + ': ' + str(scores[x]))
    


    
    