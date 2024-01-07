"""
Task: Write a Python script that calculates the teams that (within the same season) remained unbeaten at home matches. 
The resulting pickle file must contain a list with the name(s) of the teams. 
If a given team remains unbeaten for several different reasons, then it must appears as many times in the output list.
"""

import csv
import pickle

match_file = 'intro_course/intro_group_project/Match.csv'
team_file = 'intro_course/intro_group_project/Team.csv'

unbeaten_teams_by_season = {}
beaten_teams_by_season = {}

with open(match_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        season = row['season']
        home_team = row['home_team_api_id']
        home_goals = int(row['home_team_goal'])
        away_goals = int(row['away_team_goal'])

        if season not in unbeaten_teams_by_season:
            unbeaten_teams_by_season[season] = set()
            beaten_teams_by_season[season] = set()

        if home_goals < away_goals:
            beaten_teams_by_season[season].add(home_team)
            unbeaten_teams_by_season[season].discard(home_team)
        else:
            if home_team not in beaten_teams_by_season[season]:
                unbeaten_teams_by_season[season].add(home_team)                                                

team_names = {}

with open(team_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        team_id = row['team_api_id']
        team_name = row['team_long_name']
        team_names[team_id] = team_name

unbeaten_teams_list = [
    team_names.get(team, 'Unknown Team')
    for season in unbeaten_teams_by_season
    for team in unbeaten_teams_by_season[season]
]

with open('query1.pickle', 'wb') as file:
    pickle.dump(unbeaten_teams_list, file)
