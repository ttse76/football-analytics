import Utils.StatsUtil as util
from random import gauss

def simGame(away_scores, home_scores):
    away_points = (gauss(away_scores['team'], away_scores['stdev_team']) + gauss(away_scores['away'], away_scores['stdev_away'])) / 2
    away_opp_points = (gauss(home_scores['opp'], home_scores['stdev_opp']) + gauss(home_scores['opp_home'], home_scores['stdev_opp_home'])) / 2

    home_points = (gauss(home_scores['team'], home_scores['stdev_team']) + gauss(home_scores['home'], home_scores['stdev_home'])) / 2
    home_opp_points = gauss(away_scores['opp'], away_scores['stdev_opp']) + gauss(away_scores['opp_away'], away_scores['stdev_opp_away']) / 2
    away_score = (away_points + away_opp_points) / 2
    home_score = (home_points + home_opp_points) / 2
    if(away_score > home_score):
        return {
            'away': away_score,
            'home': home_score,
            'result': -1
        }
    elif(away_score < home_score):
        return {
            'away': away_score,
            'home': home_score,
            'result': 1
        }
    else:
        return {
            'away': away_score,
            'home': home_score,
            'result': 0
        }

def out(results, away, home):
    print(away + ' win: ' + str(results['away']) + '%')
    print(home + ' win: ' + str(results['home']) + '%')
    print('Tie: ' + str(results['tie']) + '%')
    print('Avg Score: ' + str(results['away_score']) + ' - ' + str(results['home_score']))
    print('\n')

def run(away_info, home_info):
    away_scores = util.getScoreStats(away_info)
    home_scores = util.getScoreStats(home_info)
    print('away: ' + str(away_scores) + '\nhome: ' + str(home_scores) + '\n\n')
    home_wins = 0
    away_wins = 0
    home_score = 0
    away_score = 0
    ties = 0
    num_games = util.get_num_games()
    for i in range(num_games):
        result = simGame(away_scores, home_scores)
        away_score = away_score + result['away']
        home_score = home_score + result['home']
        outcome = result['result']
        if outcome == 1:
            home_wins = home_wins + 1
        elif outcome == -1:
            away_wins = away_wins + 1
        else:
            ties = ties + 1
    res = {}
    res['home'] = round((home_wins/num_games) * 100, 4)
    res['home_score'] = round(home_score/num_games)
    res['away'] = round((away_wins/num_games) * 100, 4)
    res['away_score'] = round(away_score/num_games)
    res['tie'] = round((ties/num_games) * 100, 4)
    res['num_games'] = num_games
    return res