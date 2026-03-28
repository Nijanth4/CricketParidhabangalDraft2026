def validate_team(team):
    roles = {"WK":0, "AR":0, "BAT":0, "BOWL":0}
    bat_bowl_sum = 0
    overseas = 0

    for p in team:
        roles[p["role"]] += 1
        bat_bowl_sum += p["bat"] + p["bowl"]
        overseas += p["overseas"]

    if len(team) != 11:
        return "Team must have 11 players"

    if roles["WK"] < 1 or roles["AR"] < 1 or roles["BAT"] < 2 or roles["BOWL"] < 2:
        return "Role distribution invalid"

    if bat_bowl_sum < 55:
        return "Batters + Bowlers sum must be ≥ 55"

    if overseas > 46:
        return "Overseas limit exceeded"

    return "OK"
