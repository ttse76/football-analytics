import Utils.StatsUtil as util
from random import gauss

NUM_GAMES=10000

def simGame(home_scores, away_scores):
    home_score = int(round((gauss(home_scores['team'], home_scores['stdev_team']) + gauss(away_scores['opp'], away_scores['stdev_opp']))/2))
    away_score = int(round((gauss(away_scores['team'], away_scores['stdev_team']) + gauss(home_scores['opp'], home_scores['stdev_opp']))/2))
    if(away_score > home_score):
        return -1
    elif(away_score < home_score):
        return 1
    else:
        return 0


def modelA(away_info, home_info):
    home_scores = util.getScoreStats(home_info)
    away_scores = util.getScoreStats(away_info)
    results = []
    home_wins = 0
    away_wins = 0
    ties = 0
    for i in range(NUM_GAMES):
        result = simGame(home_scores, away_scores)
        results.append(result)
        if result == 1:
            home_wins = home_wins + 1
        elif result == -1:
            away_wins = away_wins + 1
        else:
            ties = ties + 1
    res = {}
    res['home'] = round((home_wins/NUM_GAMES) * 100, 4)
    res['away'] = round((away_wins/NUM_GAMES) * 100, 4)
    res['tie'] = round((ties/NUM_GAMES) * 100, 4)
    res['num_games'] = NUM_GAMES
    return res
