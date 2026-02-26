data = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 2,
            },
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
            },
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {
            "type_item": "weapon",
            "value": 150,
            "rarity": "common",
        },
        "quantum_ring": {
            "type_item": "accessory",
            "value": 500,
            "rarity": "rare",
        },
        "health_byte": {
            "type_item": "consumable",
            "value": 25,
            "rarity": "common",
        },
        "data_crystal": {
            "type_item": "material",
            "value": 1000,
            "rarity": "legendary",
        },
        "code_bow": {
            "type_item": "weapon",
            "value": 200,
            "rarity": "uncommon",
        },
    },
}


def player_inventory(player_name, player_data, catalog):
    """Displays the inventory of a player with item details."""
    print(f"=== {player_name.capitalize()}'s Inventory ===")
    categories = {}
    for item, qty in player_data["items"].items():
        item_info = catalog.get(item, {})
        item_type = item_info.get("type_item", "unknown")
        rarity = item_info.get("rarity", "common")
        value = item_info.get("value", 0)
        line_value = qty * value
        categories[item_type] = categories.get(item_type, 0) + qty
        print(
            f"{item} ({item_type}, {rarity}): {qty}x"
            f" @ {value} gold each = {line_value} gold"
        )
    print(f"\nInventory value: {player_data['total_value']} gold")
    print(f"Item count: {player_data['item_count']} items")
    parts = []
    for k, v in categories.items():
        parts.append(k + "(" + str(v) + ")")
    all_categories = ", ".join(parts)
    print(f"Categories: {all_categories}")


def transaction(giver, receiver, item, qty, players, catalog):
    """Transfers items between two players and updates values."""
    giver_items = players[giver]["items"]
    receiver_items = players[receiver]["items"]

    if giver_items.get(item, 0) < qty:
        print("Transaction failed: insufficient items.")
        return

    giver_items[item] = giver_items.get(item, 0) - qty
    receiver_items[item] = receiver_items.get(item, 0) + qty

    item_value = catalog.get(item, {}).get("value", 0)
    players[giver]["total_value"] -= item_value * qty
    players[receiver]["total_value"] += item_value * qty
    players[giver]["item_count"] -= qty
    players[receiver]["item_count"] += qty

    print("Transaction successful!")


def get_most_valuable(players):
    """Returns the player with the highest total inventory value."""
    if not players:
        return None, 0
    best_player = None
    best_value = 0
    for name, player_data in players.items():
        if player_data["total_value"] > best_value:
            best_value = player_data["total_value"]
            best_player = name
    return best_player, players[best_player]


def get_most_items(players):
    """Returns the player with the most items in inventory."""
    if not players:
        return None, 0
    best_player = None
    best_count = 0
    for name, player_data in players.items():
        if player_data["item_count"] > best_count:
            best_count = player_data["item_count"]
            best_player = name
    return best_player, players[best_player]


def get_rare_items(players, catalog):
    """Returns list of rare and legendary items owned by players."""
    rare = []
    for item, info in catalog.items():
        if info.get("rarity") in ("rare", "legendary"):
            for player in players.values():
                if player["items"].get(item, 0) > 0:
                    if item not in rare:
                        rare.append(item)
                    break
    return rare


def main():
    """Main function demonstrating the inventory system."""
    players = data["players"]
    catalog = data["catalog"]
    player_name = 'alice'

    if player_name not in players:
        print(f"Player '{player_name}' not found.")
        return

    print("=== Player Inventory System ===\n")
    player_inventory(player_name, players[player_name], catalog)

    giver = player_name
    if player_name.lower() != "bob":
        receiver = "bob"
    else:
        receiver = "alice"
    transfer_item = "pixel_sword"
    transfer_qty = 1

    print(f"\n=== Transaction: {giver.capitalize()} gives "
          f"{receiver.capitalize()} {transfer_qty} {transfer_item} ===")
    transaction(giver, receiver, transfer_item, transfer_qty, players, catalog)

    print("\n=== Updated Inventories ===")
    print(
        f"{giver.capitalize()} {transfer_item}:"
        f" {players[giver]['items'].get(transfer_item, 0)}"
    )
    print(
        f"{receiver.capitalize()} {transfer_item}:"
        f" {players[receiver]['items'].get(transfer_item, 0)}"
    )

    print("\n=== Inventory Analytics ===")
    mvp_name, mvp_data = get_most_valuable(players)
    print(f"Most valuable player: {mvp_name.capitalize()} "
          f"({mvp_data['total_value']} gold)")

    mip_name, mip_data = get_most_items(players)
    print(f"Most items: {mip_name.capitalize()} "
          f"({mip_data['item_count']} items)")

    rare = get_rare_items(players, catalog)
    print(f"Rarest items: {', '.join(rare)}")


if __name__ == "__main__":
    main()
