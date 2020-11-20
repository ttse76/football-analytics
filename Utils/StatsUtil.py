from sportsreference.nfl.teams import Teams
from sportsreference.nfl.schedule import Schedule
from sportsreference.nfl.boxscore import Boxscore
from sys import exit
import Utils.TeamAbbreviations as ab
from statistics import stdev

# Constants

__YEAR = 2020
__NUMWEEKS = 16
__NUM_GAMES= 10000

def set_year(year):
    __YEAR = year

def set_weeks(weeks):
    __NUMWEEKS = weeks

def set_num_games(num_games):
    __NUM_GAMES = num_games

def get_num_games():
    return __NUM_GAMES

# gets Team object for set team and year
def getSeason(team, year=__YEAR):
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

# For this function, home = score of team we are compiling for, away = opponent scores
def getScoreStats(team_info):
    games = getBoxScoreIndexes(team_info)
    num_games = len(games)
    team_total = 0
    team_scores = []
    opp_total = 0
    opp_scores = []
    scores = {}
    for uri in games:
        game_data = Boxscore(uri)
        home_points = float(game_data.home_points)
        away_points = float(game_data.away_points)
        if game_data.away_abbreviation.upper() == team_info.abbreviation.upper():
            team_total = team_total + away_points
            team_scores.append(away_points)
            opp_total = opp_total + home_points
            opp_scores.append(home_points)
        elif game_data.home_abbreviation.upper() == team_info.abbreviation.upper():
            team_total = team_total + home_points
            team_scores.append(home_points)
            opp_total = opp_total + away_points
            opp_scores.append(away_points)

    scores['team'] = team_total / num_games
    scores['stdev_team'] = stdev(team_scores)
    scores['opp'] = opp_total / num_games
    scores['stdev_opp'] = stdev(opp_scores)
    return scores