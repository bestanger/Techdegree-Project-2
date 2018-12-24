import csv

player_list = []  # list to populate with data from csv
dragons = []  # list to populate with players on dragons team
sharks = []  # list to populate with players on sharks team
raptors = []  # list to populate with players on the raptors team
# dictionary of team name strings mapped to lists of team players
teams = {'Dragons': dragons, 'Sharks': sharks, 'Raptors': raptors}


def build_league():

    """Creates a league of evenly matched teams"""

    # read in data from csv file
    with open('soccer_players.csv', newline='') as players:
        player_reader = csv.reader(players, delimiter=',')
        rows = list(player_reader)
        for row in rows[1:]:
            player_list.append([str(row[0]), str(row[1]),
                                str(row[2]), str(row[3])])

    # split list into players with and without experience
    yes = [player for player in player_list if player[2] == 'YES']
    no = [player for player in player_list if player[2] == 'NO']

    # assign players to teams, iterate through teams
    for team in teams.values():
        # assign players with experience to teams
        while len(team) < int(len(yes) / 3):
            team.append(yes[0])
            del yes[0]

        # assign players without experience to teams
        while len(team) < (int(len(yes) / 3) + int(len(no) / 3)):
            team.append(no[0])
            del no[0]

    # write teams to file, teams.txt
    file = open("teams.txt", "w")
    # iterate over teams
    for team in teams:
        # write team name an a break under team name
        file.write(team + "\n======================\n")
        # iterate over players
        for player in teams[team]:
            # write player name and stats
            file.write(', '.join(player) + "\n")
        file.write("\n\n")


def greetings(teams):

    """Creates a customized greeting to send to players parents;
    Informs them of which team they are on, and when the first practice is"""

    # iterate over teams
    for team in teams:
        # iterate over players in team
        for player in teams[team]:
            # open file named after player on team, and write to it
            file = open(player[0] + ".txt", "w")
            # write a greeting to players parents, regarding team placement
            file.write(
                "Hello, " + player[3] + "! We are pleased to announce that " +
                "your child, " + player[0] + "," +
                " is on the " + team + " for this soccer season!"
                "\n\nThe team's first practice is scheduled for" +
                " next Wednesday, at 6pm. See you then!")

# execute if it the file is called
if __name__ == "__main__":
    build_league()
    greetings(teams)
