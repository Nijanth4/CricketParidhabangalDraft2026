def calculate_points(player_stats):
    points = 0

    points += player_stats["runs"]
    points += player_stats["fours"] * 1
    points += player_stats["sixes"] * 2
    points += player_stats["wickets"] * 25
    points += player_stats["maidens"] * 8
    points += player_stats["catches"] * 8
    points += player_stats["stumpings"] * 12

    if player_stats["duck"]:
        points -= 2

    return points