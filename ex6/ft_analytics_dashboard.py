data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": [
        "casual",
        "competitive",
        "ranked",
    ],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


def list_comprehension(players, sessions):
    """Demonstrates list comprehensions for filtering and transforming data."""
    print("\n=== List Comprehension Examples ===")
    high_scorers = [
        player for player, score in players.items()
        if score["total_score"] > 3000
        ]
    print(f"High scorers (>3000): {high_scorers}")
    scores_doubled = [
        (score["total_score"] * 2) for _, score in players.items()
        if score["total_score"] > 0
    ]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [
        name for name in players
        if (s['player'] == name for s in sessions)
    ]
    print(f"Active players: {active_players}")


def dict_comprehension(players):
    """Demonstrates dict comprehensions for creating mappings."""
    print("\n=== Dict Comprehension Examples ===")
    player_score = {
        player: score["total_score"] for player, score in players.items()
    }
    print(f"Player scores: {player_score}")
    categorized = {
        name: 'high' if info['total_score'] > 5000
        else 'medium' if info['total_score'] > 2000
        else 'low'
        for name, info in players.items()
    }
    score_categories = {
        category: list(categorized.values()).count(category)
        for category in ['high', 'medium', 'low']
    }
    print(f"Score categories: {score_categories}")
    achievements_count = {
        player: count['achievements_count']
        for player, count in players.items()
    }
    print(f"Achievement counts: {achievements_count}")


def set_comprehension(players, game_modes, achievements):
    """Demonstrates set comprehensions for finding unique values."""
    print("\n=== Set Comprehension Examples ===")
    unique_players = {
        player for player in players
    }
    print(f"Unique players: {unique_players}")
    unique_achievements = {
        achievement for achievement in achievements
    }
    print(f"Unique achievements: {unique_achievements}")
    unique_game_modes = {
        game_mode for game_mode in game_modes
    }
    print(f"Unique game modes: {unique_game_modes}")


def combined_comprehensions(players, achievements):
    """Combines all comprehension types for final analytics."""
    print("\n=== Combined Analysis ===")
    total_players = len({player for player in players})
    print(f"Total player: {total_players}")
    total_achievements = len({achievement for achievement in achievements})
    print(f"Total unique achievements: {total_achievements}")
    all_score = sum([score['total_score'] for _, score in players.items()])
    average_score = all_score / total_players
    print(f"Average score: {average_score:.1f}")
    best_name = None
    best_score = 0
    for player, score in players.items():
        if score['total_score'] > best_score:
            best_score = score['total_score']
            best_name = player
    print(f"Top performer: {best_name} "
          f"({players[best_name]['total_score']}"
          f" points, {players[best_name]['achievements_count']}"
          f" achievements)")


def main():
    """Main function demonstrating the analytics dashboard."""
    players = data['players']
    sessions = data['sessions']
    game_modes = data['game_modes']
    achievements = data['achievements']

    print("=== Game Analytics Dashboard ===")

    list_comprehension(players, sessions)

    dict_comprehension(players)

    set_comprehension(players, game_modes, achievements)

    combined_comprehensions(players, achievements)


if __name__ == "__main__":
    main()
