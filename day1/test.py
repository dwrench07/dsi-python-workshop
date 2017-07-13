import os
from collections import defaultdict
from datetime import datetime


def read_game_info():
    for folder, subs, files in os.walk("data/worldcup/"):
        print("Searching: {}\n".format(os.path.relpath(folder)))
        print("Found: {} files.".format(len(files)))
        for filename in files:
            with open(os.path.join(folder, filename), 'r') as src:
                file_contents = src.readlines()
                # print(file_contents)

                match_date = datetime.strptime(file_contents[0].strip(), '%d %b %Y - %H:%M').strftime('%b %d')
                _ = file_contents[1].strip()  # Ignoring Stadium
                team = file_contents[2].strip()
                opponent = file_contents[3].strip()
                team_score, opp_score = file_contents[4].strip().split("-")

                # Mar 29: Belize (1) - Cayman Islands (1)
                print(f"{match_date}: {team} ({team_score}) - {opponent} ({opp_score})")

                # data = defaultdict(dict)
                # temp_dict = data[team]
                #
                # temp_dict["games"] = defaultdict(list)
                # temp_dict["games"].append(match_date, team, team_score, opponent, opp_score)
                #
                # temp_dict['goals'] = data[team]["goals"] + team_score
                # temp_dict["wins"] =
                # temp_dict["losses"] =
                # temp_dict["ties"] =


def game(team, team_score, opp_score):
    if team_score == opp_score:
        team["ties"] += 1
    elif team_score < opp_score:
        team["losses"] += 1
    else:
        team["wins"] += 1


read_game_info()
