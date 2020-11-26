import Utils.StatsUtil as util
import pandas as pd
import Utils.TeamAbbreviations as ab
import sys
import Models.ModelA as a
import Models.ModelB as b

YEAR = 2020
WEEKS = 16

AWAY='HOU'
HOME='DET'

models = {
    'a': a,
    'b': b
}

def select_model(model_selection):
    model = models.get(model_selection.lower(), lambda: "Invlaid")
    if model == 'Invalid':
        print('model invalid')
        sys.exit(1)
    return model



def set_options():
    util.set_year(YEAR)
    util.set_weeks(WEEKS)

# away team, away win %, away score, home team, home win %, home score, tie %
def generate_data(results, away, home):
    return away + ',' + str(results['away']) + ',' + str(results['away_score']) + ',' + home + ',' + str(results['home']) + ',' + str(results['home_score']) + ',' + str(results['tie'])


if __name__ == '__main__':
    '''
    if len(sys.argv) < 2:
        print('Requires model selection')
        sys.exit(1)
    model_selection = str(sys.argv[1])
    '''
    away_info = util.getSeason(AWAY)
    home_info = util.getSeason(HOME)

    '''
    away_scores = util.getScoreStats(away_info)
    home_scores = util.getScoreStats(home_info)
    print(str(away_scores['away']) + ':' + str(away_scores['team']))
    print(b.calcAdv(away_scores, 'away'))
    print(str(home_scores['home']) + ':' + str(home_scores['team']))
    print(b.calcAdv(home_scores, 'home'))
    '''

    resultsA = a.run(away_info, home_info)
    print('Model A:\n')
    a.out(resultsA, AWAY, HOME)
    resultsB = b.run(away_info, home_info)
    print('Model B:\n')
    b.out(resultsB, AWAY, HOME)
