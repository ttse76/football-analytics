from sportsreference.nfl.teams import Teams
from sportsreference.nfl.schedule import Schedule
from sportsreference.nfl.boxscore import Boxscore
from sys import exit
import TeamAbbreviations as ab
from statistics import stdev


# Constants

__YEAR = 2020
__NUMWEEKS = 16

def set_year(year):
    __YEAR = year

def set_weeks(weeks):
    __NUMWEEKS = weeks

# gets Team object for set team and year
def getSeason(team, year=__YEAR):
    print('TEAM: ' + team)
    team_index = ab.get(team)
    if team_index == 'DNE':
        print('ERROR: ' + team + ' not valid')
        exit(1)
    teams = Teams(str(year))
    return teams(team_index)

def getBoxScoreIndexes(team_info):
    indexes = team_info.schedule.dataframe.boxscore_index
    games_played = team_info.games_played
    index_list = []
    
    for x in range(0, min(__NUMWEEKS, games_played)):
        index_list.append(indexes[x])

    if len(index_list) == __NUMWEEKS:
        return index_list
    team_infoLY = getSeason(team_info.abbreviation, __YEAR - 1)
    indexesLY = team_infoLY.schedule.dataframe.boxscore_index

    for x in range(len(indexesLY)-1, games_played - 1, -1):
        index_list.append(indexesLY[x])
    return index_list

    

def getScoreStats(team_info):
    games = getBoxScoreIndexes(team_info)
    scores = {}
    total_score = 0
    away_score = 0
    home_score = 0
    num_home = 0
    num_away = 0
    num_total = 0
    away_scores = []
    home_scores = []
    all_scores = []
    for uri in games:
        game_data = Boxscore(uri)
        if game_data.away_abbreviation.upper() == team_info.abbreviation:
            points = float(game_data.away_points)
            away_scores.append(points)
            all_scores.append(points)
            away_score = away_score + points
            total_score = total_score + points
            num_away = num_away + 1
        elif game_data.home_abbreviation.upper() == team_info.abbreviation:
            points = float(game_data.home_points)
            home_scores.append(points)
            all_scores.append(points)
            home_score = home_score + points
            total_score = total_score + points
            num_home = num_home + 1
        num_total = num_total + 1
    
    scores['home'] = home_score / num_home
    scores['stdev_home'] = stdev(home_scores)
    scores['away'] = away_score / num_away
    scores['stdev_away'] = stdev(away_scores)
    scores['total'] = total_score / num_total
    scores['stdev_total'] = stdev(all_scores)
    return scores



