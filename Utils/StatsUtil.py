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
__WEEKS_BACK = 0

def set_year(year):
    __YEAR = year

def set_weeks(weeks):
    __NUMWEEKS = weeks

def set_num_games(num_games):
    __NUM_GAMES = num_games

def set_weeks_back(weeks_back):
    __WEEKS_BACK = weeks_back

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
    start_week = games_played - __WEEKS_BACK
    index_list = []
    
    for x in range(0, min(__NUMWEEKS, start_week)):
        index_list.append(indexes[x])

    if len(index_list) == __NUMWEEKS:
        return index_list
    team_infoLY = getSeason(team_info.abbreviation, __YEAR - 1)
    indexesLY = team_infoLY.schedule.dataframe.boxscore_index

    for x in range(len(indexesLY)-1, start_week - 1, -1):
        index_list.append(indexesLY[x])
    return index_list

def getScoreStats(team_info):
    games = getBoxScoreIndexes(team_info)
    num_games = len(games)
    home_total=0
    away_total=0
    team_total = 0
    home_scores = []
    away_scores = []
    team_scores = []
    opp_total = 0
    opp_home = 0
    opp_away = 0
    opp_home_scores = []
    opp_away_scores = []
    opp_scores = []
    scores = {}
    for uri in games:
        game_data = Boxscore(uri)
        home_points = float(game_data.home_points)
        away_points = float(game_data.away_points)

        # if team was away this game
        if game_data.away_abbreviation.upper() == team_info.abbreviation.upper():
            team_total = team_total + away_points
            team_scores.append(away_points)
            away_scores.append(away_points)
            away_total = away_total + away_points
            opp_total = opp_total + home_points
            opp_home = opp_home + home_points
            opp_home_scores.append(home_points)
            opp_scores.append(home_points)

        # if team was home this game
        elif game_data.home_abbreviation.upper() == team_info.abbreviation.upper():
            team_total = team_total + home_points
            home_scores.append(home_points)
            home_total = home_total + home_points
            team_scores.append(home_points)
            opp_total = opp_total + away_points
            opp_scores.append(away_points)
            opp_away = opp_away + away_points
            opp_away_scores.append(away_points)

    # SRS rating for team
    scores['rating'] = team_info.simple_rating_system
    
    # Points scored at home
    scores['home'] = home_total / len(home_scores)

    # Points socred away
    scores['away'] = away_total / len(away_scores)

    # Standard deviation of home points
    scores['stdev_home'] = stdev(home_scores)

    # Standard deviation of away points
    scores['stdev_away'] = stdev(away_scores)

    # Points scored over all games
    scores['team'] = team_total / len(team_scores)

    # Standard deviation of all games
    scores['stdev_team'] = stdev(team_scores)

    # Points socred by opponenets
    scores['opp'] = opp_total / len(opp_scores)

    # standard deviation of points scored by opponents
    scores['stdev_opp'] = stdev(opp_scores)

    # Points scored by opponent when opponent is home (team is away)
    scores['opp_home'] = opp_home / len(opp_home_scores)
    scores['stdev_opp_home'] = stdev(opp_home_scores)

    # Points scored by opponent when opponenet is away (team is home)
    scores['opp_away'] = opp_away / len(opp_away_scores)
    scores['stdev_opp_away'] = stdev(opp_away_scores)

    return scores