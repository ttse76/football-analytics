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
    if len(sys.argv) == 2:
        WEEKS = int(sys.argv[1])
    elif len(sys.argv) == 3:
        WEEKS = int(sys.argv[1])
        YEAR = int(sys.argv[2])
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
    print('Number of Games Simulated: 10000\n\n')
    for match in matchups:
        away_info = util.getSeason(match[0])
        home_info = util.getSeason(match[1])
        results = Models.modelA(away_info, home_info)
        print(match[0] + ' win: ' + str(results['away']) + '%')
        print(match[1] + ' win: ' + str(results['home']) + '%')
        print('Tie: ' + str(results['tie']) + '%')
        print('\n')
