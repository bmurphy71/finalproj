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
#########################################################################################
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
######################################################################################################
# Add players to each team
for team, team_name in zip(teams, team_names):
    for _ in range(6):  # Set 6 players per team
        player = create_player()
        team.append(player)

# Function to display players in a team
def display_players(team):
    for player in team:
        print(f"{player['name']} - {player['position']} - Overall: {player['overall']}")

# Function to trade players between teams
def trade_players():
    print("Teams:")
    for i, team_name in enumerate(team_names):
        print(f"{i+1}. {team_name}")
    try:
        user_input = int(input("Choose a team to trade from (enter number): ")) - 1
        if user_input < 0 or user_input >= len(teams):
            print("Invalid team choice. Please choose a valid team.")
            return
        team_from = teams[user_input]

        print(f"Players in {team_names[user_input]}:")
        display_players(team_from)

        player_index = int(input("Choose the player index to trade: "))
        if player_index < 0 or player_index >= len(team_from):
            print("Invalid player index. Please choose a valid index.")
            return
        player_to_trade = team_from.pop(player_index)

        user_input = int(input("Choose a team to trade to (enter number): ")) - 1
        if user_input < 0 or user_input >= len(teams):
            print("Invalid team choice. Please choose a valid team.")
            return
        team_to = teams[user_input]

        print(f"Players in {team_names[user_input]}:")
        display_players(team_to)

        player_return_index = int(input("Choose the player index to receive in return: "))
        if player_return_index < 0 or player_return_index >= len(team_to):
            print("Invalid player index. Please choose a valid index.")
            return
        player_returned = team_to.pop(player_return_index)

        # Perform the trade
        team_from.append(player_returned)
        team_to.append(player_to_trade)

        print("Trade successful!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main trading loop
while True:
    print("\nTrade Simulator Menu:")
    print("1. Trade Players")
    print("2. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        trade_players()
    elif choice == "2":
        print("Exiting Trade Simulator.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

