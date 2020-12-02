import Utils.StatsUtil as util
import pandas as pd
import Utils.TeamAbbreviations as ab
import Models.ModelA as a
import Models.ModelB as b

YEAR = 2020
Week = 16

DIV = ['NYG', 'PHI', 'WAS', 'DAL']

NYG = 'NYG'
NYG_record = [4,7]
NYG_div = [3,2]
NYG_sch = [['SEA', 'away'], ['ARI', 'home'], ['CLE', 'home'], ['BAL', 'away'], ['DAL', 'home']]

WAS = 'WAS'
WAS_record = [4,7]
WAS_div = [3,2]
WAS_sch = [['PIT', 'away'], ['SF', 'away'], ['SEA', 'home'], ['CAR', 'home'], ['PHI', 'away']]

PHI = 'PHI'
PHI_record = [3,7]
PHI_div=[2,2]
PHI_sch = [['GB', 'away'], ['NO', 'home'], ['ARI', 'away'], ['DAL', 'away'], ['WAS', 'home']]

DAL = 'DAL'
DAL_record = [3,8]
DAL_div = [1,3]
DAL_sch = [['BAL', 'away'], ['CIN', 'away'], ['SF', 'home'], ['PHI', 'home'], ['NYG', 'away']]

teams = {}

def simGames(team_info, team_record, team_div, team_sch):
    for game in team_sch:
        if game[0] in teams.keys():
            opp_info = teams[game[0]]
        else:
            opp_info = util.getSeason(game[0])
            teams[game[0]] = opp_info
        if game[1] == 'away':
            results = b.run(team_info, opp_info)
            if results['away'] > results['home']:
                team_record[0] = team_record[0] + 1
                if game[0] in DIV:
                    team_div[0] = team_div[0] + 1
            else:
                team_record[1] = team_record[1] + 1
                if game[0] in DIV:
                    team_div[1] = team_div[1] + 1
        else:
            results = b.run(opp_info, team_info)
            if results['away'] > results['home']:
                team_record[1] = team_record[1] + 1
                if game[0] in DIV:
                    team_div[1] = team_div[1] + 1
            else:
                team_record[0] = team_record[0] + 1
                if game[0] in DIV:
                    team_div[0] = team_div[0] + 1
    return {
        'record': team_record,
        'div': team_div
    }

def out(team, div, rec):
    print('TEAM: ' + team)
    print("rec overall: " + rec)
    print('division: ' + div)

if __name__ == '__main__':
    nyg_res = simGames(util.getSeason('NYG'), NYG_record, NYG_div, NYG_sch)
    out('NYG', nyg_res['div'], nyg_res['record'])

    phi_res = simGames(util.getSeason('PHI'), PHI_record, PHI_div, PHI_sch)
    out('PHI', phi_res['div'], phi_res['record'])

    was_res = simGames(util.getSeason('WAS'), WAS_record, WAS_div, WAS_sch)
    out('WAS', was_res['div'], was_res['record'])

    phi_res = simGames(util.getSeason('PHI'), PHI_record, PHI_div, PHI_sch)
    out('PHI', phi_res['div'], phi_res['record'])