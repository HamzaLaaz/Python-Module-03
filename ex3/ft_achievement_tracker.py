data = {
   "alice": [
      "first_blood",
      "pixel_perfect",
      "speed_runner",
      "first_blood",
      "first_blood"
   ],
   "bob": [
      "level_master",
      "boss_hunter",
      "treasure_seeker",
      "level_master",
      "level_master",
      "first_blood"
   ],
   "charlie": [
      "treasure_seeker",
      "boss_hunter",
      "combo_king",
      "first_blood",
      "boss_hunter",
      "first_blood",
      "boss_hunter",
      "first_blood"
   ],
   "diana": [
      "first_blood",
      "combo_king",
      "level_master",
      "treasure_seeker",
      "speed_runner",
      "combo_king",
      "combo_king",
      "level_master"
   ],
   "eve": [
      "level_master",
      "treasure_seeker",
      "first_blood",
      "treasure_seeker",
      "first_blood",
      "treasure_seeker"
   ],
   "frank": [
      "explorer",
      "boss_hunter",
      "first_blood",
      "explorer",
      "first_blood",
      "boss_hunter"
   ]
}


def main():
    """Main function demonstrating achievement tracking using sets."""
    print("=== Achievement Tracker System ===\n")
    items = ["alice", "bob", "charlie", "diana", "eve", "frank"]

    for name in items:
        print(f"Player {name} achievements: {set(data[name])}")

    print("\n=== Achievement Analytics ===")
    all_achievements = set()
    for name in items:
        all_achievements = all_achievements.union(set(data[name]))
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")
    common_all = set(data[items[0]])
    for name in items[1:]:
        common_all = common_all.intersection(set(data[name]))
    print(f"Common to all players: {common_all}")
    rare_achievements = set()
    for achievement in all_achievements:
        count = 0
        for name in items:
            if achievement in set(data[name]):
                count += 1
        if count == 1:
            rare_achievements.add(achievement)
    print(f"Rare achievements (1 player): {rare_achievements}\n")
    alice = set(data["alice"])
    bob = set(data["bob"])
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
