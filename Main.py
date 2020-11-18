import Utils.StatsUtil as util
import pandas as pd
import Utils.TeamAbbreviations as ab
import sys
import Models

YEAR = 2020
WEEKS = 16
AWAY_TEAM = 'NYJ'
HOME_TEAM = 'PIT'

def set_options():
    util.set_year(YEAR)
    util.set_weeks(WEEKS)

if __name__ == '__main__':
    set_options()
    games_file = open('games.txt', 'r')
    matchups = []

    for x in games_file:
        matchup = x.strip().split('@')
        for y in matchup:
            if ab.get(y) == 'DNE':
                print('ERROR: ' + y + ' not valid abbreviation')
                sys.exit(1)
        matchups.append(matchup)
    games_file.close()
    for match in matchups:
        away_info = util.getSeason(match[0])
        home_info = util.getSeason(match[1])
        results = Models.modelA(away_info, home_info)
        print('Number of Games Simulated: ' + str(results['num_games']))
        print(match[0] + ' win: ' + str(results['away']) + '%')
        print(match[1] + ' win: ' + str(results['home']) + '%')
        print('Tie: ' + str(results['tie']) + '%')
 
    '''
    home_team_info = util.getSeason(HOME_TEAM)
    away_team_info = util.getSeason(AWAY_TEAM)

    res = Models.modelA(away_team_info, home_team_info)
    out(res)
    '''


