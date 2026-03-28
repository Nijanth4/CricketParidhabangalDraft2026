import pandas as pd

LEAGUE = {}

def add_score(user, match_no, points):
    if user not in LEAGUE:
        LEAGUE[user] = {}

    LEAGUE[user][match_no] = points

def leaderboard():
    data = []
    for user, matches in LEAGUE.items():
        total = sum(matches.values())
        data.append({"User": user, "Points": total})

    return pd.DataFrame(data).sort_values("Points", ascending=False)