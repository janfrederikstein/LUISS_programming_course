"""
Task: Write a Python script that calculates the two teams that faced each other the most (counting both home and away matches). 
The resulting pickle file must contain a list with the name of the two teams.

Constraint: You are not allowed to use any third-party library. 
You can only use libraries and modules belonging to the Python Standard Library.
"""

import csv
import pickle

match_file = 'intro_course/intro_group_project/Match.csv'
team_file = 'intro_course/intro_group_project/Team.csv'

all_matches = {}

with open(match_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        home_team = row['home_team_api_id']
        away_team = row['away_team_api_id']

        match_pair = tuple(sorted([home_team, away_team]))
        all_matches[match_pair] = all_matches.get(match_pair, 0) + 1

highest_match_count = max(all_matches.values())
most_frequent_matchups = [matchup for matchup, count in all_matches.items() if count == highest_match_count]

translated_teams = {}

with open(team_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        team_id = row['team_api_id']
        team_name = row['team_long_name']
        translated_teams[team_id] = team_name

most_frequent_matchups_names = [[translated_teams[team_id] for team_id in matchup] for matchup in most_frequent_matchups]

with open('query3.pickle', 'wb') as file:
   pickle.dump(most_frequent_matchups_names, file)
