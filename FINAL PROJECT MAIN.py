#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:02:43 2024

@author: brendanmurphy
"""
team_names = ["Rams", "Horned Frogs", "Ragin' Cajuns", "Crimson Tide", "Patriots"]
class Player:
    def __init__(self, name, position, overall_rating):
        self.name = name
        self.position = position
        self.overall_rating = overall_rating

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

def generate_team(name, players_info):
    team = Team(name)
    for player_info in players_info:
        player = Player(*player_info)
        team.add_player(player)
    return team

# Predefined player information
players_info = [
    ("Deshaun", "QB", 90),
    ("James", "WR", 88),
    ("Michael", "TE", 82),
    ("John.S", "OL", 90),
    ("David.G", "DL", 87),
    ("Caleb", "LB", 83),
    ("Daniel", "CB", 86),
    ("Austin", "QB", 84),
    ("Christopher", "WR", 89),
    ("Brenden", "TE", 81),
    ("James", "OL", 80),
    ("Pete", "DL", 87),
    ("David.F","LB",94),
    ("Jacob","CB",80),
    ("Peter","QB",99),
    ("Doug","WR",80),
    ("Marvin","TE",85),
    ("Ray","OL",90),
    ("Ha-Ha","DL",94),
    ("Vince","LB",99),
    ("Aaron","CB",80),
    ("Saquan","QB",70),
    ("Jerry","WR",99),
    ("Tony","TE",99),
    ("Zach","OL",90),
    ("Joe","DL",95),
    ("Lawrence","LB",99),
    ("Deion","CB",97),  
    ("Warren","QB",90),
    ("Randy","WR",99),
    ("Rob","TE",80),
    ("Christian","OL",85),
    ("Reggie","DL",99),
    ("Luke","LB",90),
    ("Ronnie","CB",93),
]

# Generate teams with predefined players
teams = [
    generate_team("Rams", players_info[0:7]),
    generate_team("Horned Frogs", players_info[7:14]),
    generate_team("Ragin' Cajuns", players_info[14:21]),
    generate_team("Crimson Tide", players_info[21:28]),
    generate_team("Patriots", players_info[28:])
]
def display_players(team):
    for i, player in enumerate(team.players):
        print(f"{i+1}. Name: {player.name}, Position: {player.position}, Overall Rating: {player.overall_rating}")

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
        if player_index < 0 or player_index >= len(team_from.players):
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


