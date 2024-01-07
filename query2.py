"""
Task: Write a Python script that calculates the team that (within the same season) had the highest number of different 
goalkeepers in the initial squad. The resulting pickle file must contain a tuple with the name of the team and the season.

Constraint: You are not allowed to use any third-party library. 
You can only use libraries and modules belonging to the Python Standard Library.
"""

import csv
import pickle

match_file = 'intro_course/intro_group_project/Match.csv'
team_file = 'intro_course/intro_group_project/Team.csv'

goalies = {}

with open(match_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        season = row['season']
        for team_type in ['home', 'away']:
            team = row[f'{team_type}_team_api_id']
            goalie = row[f'{team_type}_player_1']

            if goalie:
                goalies.setdefault(season, {}).setdefault(team, set()).add(goalie)

most_goalies = []
max_goalie_count = 0

for season, teams in goalies.items():
    for team, players in teams.items():
        goalie_count = len(players)

        if goalie_count > max_goalie_count:
            most_goalies = [[team, season]]
            max_goalie_count = goalie_count

        elif goalie_count == max_goalie_count:
            most_goalies.append([team, season])

translated_teams = {}

with open(team_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        team_id = row['team_api_id']
        team_name = row['team_long_name']
        translated_teams[team_id] = team_name

goalies_translated = []

for team_id, season in most_goalies:
    team_name = translated_teams.get(team_id, "Unknown Team")
    goalies_translated.append((team_name, season))

goalies_final = tuple(goalies_translated)

with open('query2.pickle', 'wb') as file:
    pickle.dump(goalies_final, file)
