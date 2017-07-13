from datetime import datetime
import os
import sys
import json


def read_game_info(filename):
    """
    INPUT: string
    OUTPUT: tuple of string, string, string, int, int

    Given the filename of a game, return the time, team names and score for the
    game.

    Example File Structure:
        22 MAR 2015 - 19:00
        National Stadium
        Waterford
        Barbados - US Virgin Islands
        0-1
    """
    TXT_DATA_DIR = 'day1/data/worldcup/'
    JSON_DATA_FILE = 'day1/data/worldcup.json'

    try:
        for file in TXT_DATA_DIR:
            with open(file, 'rb') as f:
                for line in f:
                    text = line.readline()
                    team = text[0]

            with open(JSON_DATA_FILE, 'wb'):
                json.dump()



    except FileNotFoundError as e:
        print("File Not Found:")
        print(e)


def display_game(time, team, other, team_score, other_score):
    """
    INPUT: string, string, string, int, int
    OUTPUT: string

    Given the time, names of the teams and score, return a one line string
    presentation of the results.

    Example Output:
    ------------------------------------
    Mar 29: Belize (1) - Cayman Islands (1)
    Mar 25: Belize (0) - Cayman Islands (0)
    Jun 14: Belize (3) - Dominican Republic (0)
    Jun 11: Belize (2) - Dominican Republic (1)
    ------------------------------------
    """
    print("-" * 25)
    print(f"{date}: {team1} ({team_score}) - {opponent} ({opp_score})")
    print("-" * 25)


def display_summary(team, data, detailed=False):
    """
    INPUT: string, list of tuples, bool
    OUTPUT: string

    Given the data (list of tuples of game data), return a string containing
    the summary of results for the given team.

    This includes:
        # games played,
        # wins,
        # losses,
        # ties, and
        # goals scored.

    If detailed is True, also include in the string all the games for the given
    team.

    Example Output:
    ------------------------------------
    Belize played a total of 4 games.
    2 wins, 0 losses, 2 ties, 6 total goals
    ------------------------------------
    """

    print("-" * 25)
    print(f"{team} played a total of {games} games.")
    print(f"{wins} wins, {losses} losses, {ties} ties, {goals} total goals.")
    print("-" * 25)


def run(directory, team):
    """
    INPUT: string, string
    OUTPUT: None

    Given the directory where the data is stored and the team name of interest,
    read the data from the directory and display the summary of results for the
    given team.
    """
    data = []
    for filename in os.listdir(directory):
        data.append(read_game_info(os.path.join(directory, filename)))
    print(display_summary(team, data, detailed=True))


def main():
    """
    INPUT: None
    OUTPUT: None

    Get the directory name and team name from the arguments given. If arguments
    are valid, display the summary of results. Otherwise, exit the program.
    """
    error_message = "Usage: python worldcup.py directory team (e.g. python worldcup.py worldcup USA)"
    if len(sys.argv) != 3:
        print(error_message)
        exit()
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print("{0} is not a valid directory.".format(directory))
        print(error_message)
        exit()
    team = sys.argv[2]
    run(directory, team)


if __name__ == '__main__':
    main()
