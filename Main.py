import src.StatsUtil as util
import pandas as pd
import sys

YEAR = 2020
WEEKS = 16
AWAY_TEAM = 'TEN'
HOME_TEAM = 'BAL'

def set_options():
    util.set_year(YEAR)
    util.set_weeks(16)

if __name__ == '__main__':
    set_options()
    home_team_info = util.getSeason(HOME_TEAM)
    away_team_info = util.getSeason(AWAY_TEAM)

    home_scores = util.getScoreStats(home_team_info)
    away_scores = util.getScoreStats(away_team_info)

    print('Score info for ' + AWAY_TEAM)
    for score in away_scores:
        print(score + ': ' + str(away_scores[score]))
    
    print('Score info for ' + HOME_TEAM)
    for score in home_scores:
        print(score + ': ' + str(home_scores[score]))
    

    


    
    