import Utils.StatsUtil as util
import pandas as pd
import Utils.TeamAbbreviations as ab
import sys
import Models.ModelA as a
import Models.ModelB as b

YEAR = 2020
WEEKS = 16
WEEKS_BACK = 0

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
    util.set_weeks_back(WEEKS_BACK)

# away team, away win %, away score, home team, home win %, home score, tie %
def generate_data(results, away, home):
    return away + ',' + str(results['away']) + ',' + str(results['away_score']) + ',' + home + ',' + str(results['home']) + ',' + str(results['home_score']) + ',' + str(results['tie']) + '\n'


if __name__ == '__main__':
    '''
    if len(sys.argv) < 2:
        print('Requires model selection')
        sys.exit(1)
    model_selection = str(sys.argv[1])
    model = select_model(model_selection)
    if len(sys.argv) == 3:
        weeks_back = int(sys.argv[2])
    '''
    if len(sys.argv) > 1:
        WEEKS_BACK = int(sys.argv[1])

    set_options()

    games_file = open('games.txt', 'r')
    matchups = []
    team_objs = {}
    for x in games_file:
        matchup = x.strip().split('@')
        for y in matchup:
            if ab.get(y) == 'DNE':
                print('ERROR: ' + y + ' not valid abbreviation')
                sys.exit(1)
        matchups.append(matchup)
        team_objs[matchup[0]] = util.getSeason(matchup[0])
        team_objs[matchup[1]] = util.getSeason(matchup[1])
    games_file.close()
    out_fileA = open('resA.txt', 'w')

    print('Number of Games Simulated: ' + str(util.__NUM_GAMES) + '\n\n')
    print('Model A\n')
    for match in matchups:
        away_team_name = match[0]
        home_team_name = match[1]
        results = a.run(team_objs[away_team_name], team_objs[home_team_name])
        a.out(results, away_team_name, home_team_name)
        out_fileA.write(generate_data(results, away_team_name, home_team_name))
    
    out_fileA.close()
    out_fileB = open('resB.txt', 'w')
    print('Model B\n')
    for match in matchups:
        away_team_name = match[0]
        home_team_name = match[1]
        results = b.run(team_objs[away_team_name], team_objs[home_team_name])
        b.out(results, away_team_name, home_team_name)
        out_fileB.write(generate_data(results, away_team_name, home_team_name))
    out_fileB.close()



    '''
    for match in matchups:
        away_info = util.getSeason(match[0])
        home_info = util.getSeason(match[1])
        results = model.run(away_info, home_info)
        model.out(results, match[0], match[1])
        out_file.write(generate_data(results, match[0], match[1]))
    out_file.close()
    '''
