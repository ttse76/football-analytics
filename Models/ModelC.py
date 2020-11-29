import Utils.StatsUtil as util
from random import gauss

def simGame(away_scores, home_scores):
    away_score = (gauss(away_scores['team'], away_scores['stdev_team']) + gauss(home_scores['opp'], home_scores['stdev_opp']))/2
    home_score = (gauss(home_scores['team'], home_scores['stdev_team']) + gauss(away_scores['opp'], away_scores['stdev_opp']))/2
    