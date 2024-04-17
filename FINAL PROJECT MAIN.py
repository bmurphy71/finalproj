#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:02:43 2024

@author: brendanmurphy
"""

import random

# Create teams
chiefs = []
broncos = []
patriots = []
panthers = []
rams = []

teams = [chiefs, broncos, patriots, panthers, rams]
team_names = ["Chiefs", "Broncos", "Patriots", "Panthers", "Rams"]

# Function to generate a random name
def generate_random_name():
    first_names = ["Tom", "John", "Mike", "Chris", "David", "Matt", "Steve", "Alex", "Andrew", "Mark"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to create a player with random position and overall rating
def create_player():
    positions = ["QB", "WR", "TE", "OL", "DL", "LB", "CB"]
    name = generate_random_name()
    position = random.choice(positions)
    overall = random.randint(70, 99)  # Random overall rating between 70 and 99
    return {"name": name, "position": position, "overall": overall}

# Add players to each team
for team, team_name in zip(teams, team_names):
    for _ in range(6):  # Set 6 players per team
        player = create_player()
        team.append(player)

# Print players in each team
for team_name, team in zip(team_names, teams):
    print(f"{team_name} Players:")
    for player in team:
        print(f"{player['name']} - {player['position']} - Overall: {player['overall']}")
    print()


