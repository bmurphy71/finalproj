"""
Created on Wed Apr 17 17:19:05 2024

@author: Austin and Brenden
"""
class Player: #This class creates the player with name,position, and rating in that order
    def __init__(self, name, position, overall_rating):
        self.name = name
        self.position = position
        self.overall_rating = overall_rating

class Team: # this class creates our teams, which includes the name and the players
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

def generate_team(name, players_info): #this is to generate the team, by this creating this function, when we create a team and add players, it will also carry the players information, not just the name or the number in the list
    team = Team(name)
    for player_info in players_info:
        player = Player(*player_info)
        team.add_player(player)
    return team

def display_players(team): # this is for formatting, which displays the players when the team is called in that order
#the forloop represents the ith players to be added to the team, while carrying all the stats over
    for i, player in enumerate(team.players):
        print(f"{i+1}. Name: {player.name}, Position: {player.position}, Overall Rating: {player.overall_rating}")

def view_rosters(): #this is the function to view rosters, which will show all of the players we have on each team along with the attributes of each players
    print("Current Rosters:")
    for team in teams:
        print(f"\nTeam: {team.name}")
        display_players(team)

def trade_players(): # this is the trade function, which has alot so I will break it down
    print("Teams:")
    for i, team_name in enumerate(team_names):
        print(f"{i+1}. {team_name}")# this paer will give you the list of teams to trade with
    try:
        user_input = int(input("Choose a team to trade from (enter number): ")) - 1
        if user_input < 0 or user_input >= len(teams):
            print("Invalid team choice. Please choose a valid team.")
            return
        team_from = teams[user_input]#this input limits the teams you can select to being only one of the 5 teams we have

        print(f"Players in {team_names[user_input]}:") #this will then take teh team you picked and print out the players on that team so you can select one to trade
        display_players(team_from)

        player_index = int(input("Choose the player index to trade: ")) - 1
        if player_index < 0 or player_index >= len(team_from.players): #this if statement is similar to the one above and only allows you to pick the players in that range 
            print("Invalid player index. Please choose a valid index.")
            return
        player_to_trade = team_from.players.pop(player_index) #this then takes the player selected and makes it a player to trade and gives it the ability to switch lists

        user_input = int(input("Choose a team to trade to (enter number): ")) - 1 #this is the exact same thing as above but for the other team you are trading with
        if user_input < 0 or user_input >= len(teams):
            print("Invalid team choice. Please choose a valid team.")
            return
        team_to = teams[user_input]

        print(f"Players in {team_names[user_input]}:")
        display_players(team_to)

        player_return_index = int(input("Choose the player index to receive in return: ")) - 1 #same thing as above as it is teh player on this other team you are trading with
        if player_return_index < 0 or player_return_index >= len(team_to.players):
            print("Invalid player index. Please choose a valid index.")
            return
        player_returned = team_to.players.pop(player_return_index)

        # Perform the trade
        team_from.add_player(player_returned) #since we used the .pop function, this takes the players and switches them on the appropriate team and list
        team_to.add_player(player_to_trade)#this then takes the other team nd switches that player for this one

        print("Trade successful!") #then once this is complete it will say trade was succesful and print the rosters so you can see the trade
        view_rosters()

    except ValueError: #this stricts the domain and only allows to do the proper inputs
        print("Invalid input. Please enter a valid number.")

#these are our team names
team_names = ["Rams", "Horned Frogs", "Ragin' Cajuns", "Crimson Tide", "Patriots"]

# Predefined player information
#by doing this we don't have to worry about how many of certain positions and could pick the overalls instead of doing a random generator of overalls
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

#this generates each team with the first 7 players in the list, then goes to the next teams with the next 7 players
teams = [
    generate_team("Rams", players_info[0:7]),
    generate_team("Horned Frogs", players_info[7:14]),
    generate_team("Ragin' Cajuns", players_info[14:21]),
    generate_team("Crimson Tide", players_info[21:28]),
    generate_team("Patriots", players_info[28:])
]
def trading_loop(): #this function just creates the trading portal in the console
    while True:
        print("\nTrade Simulator Menu:")
        print("1. Trade Players")
        print("2. View Rosters")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            trade_players()
        elif choice == "2":
            view_rosters()
        elif choice == "3":
            print("Exiting Trade Simulator.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
while True: # this is the overall menu, since the only two options are to trade players or view the roster
    print("\Madden Menu: ")
    print("1. Trade Players ")
    print("2. View Roster ")
    main_choice = input("Choose an option")
    
    if main_choice == "1":
        trading_loop()
    elif main_choice == "2":
        view_rosters()
    else:
        print("Invalid Choice, press 1 or 2")
