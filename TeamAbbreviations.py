__TEAM_ABBREVIATIONS={
    "ARI":"CRD",
    "ATL":"ATL",
    "BAL":"RAV",
    "BUF":"BUF",
    "CAR":"CAR",
    "CHI":"CHI",
    "CIN":"CIN",
    "CLE":"CLE",
    "DAL":"DAL",
    "DEN":"DEN",
    "DET":"DET",
    "GB":"GNB",
    "HOU":"HTX",
    "IND":"CLT",
    "JAC":"JAX",
    "KC":"KAN",
    "LVR":"RAI",
    "LAR":"RAM",
    "LAC":"SDG",
    "MIA":"MIA",
    "MIN":"MIN",
    "NE":"NWE",
    "NO":"NOR",
    "NYG":"NYG",
    "NYJ":"NYJ",
    "PHI":"PHI",
    "PIT":"PIT",
    "SF":"SFO",
    "SEA":"SEA",
    "TB":"TAM",
    "TEN":"OTI",
    "WAS":"WAS"
}

def get(team):
    team = team.upper()
    if team in __TEAM_ABBREVIATIONS:
        return __TEAM_ABBREVIATIONS[team]
    else:
        if team in __TEAM_ABBREVIATIONS.values():
            return team
    return 'DNE'