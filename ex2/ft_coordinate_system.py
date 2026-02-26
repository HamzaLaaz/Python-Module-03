import math


def create_3D_position(x, y, z):
    """Creates a 3D position tuple from x, y, z coordinates."""
    return x, y, z


def calculate_distance(pos1, pos2):
    """Calculates Euclidean distance between two 3D positions."""
    (x1, y1, z1) = pos1
    (x2, y2, z2) = pos2
    dist = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    return dist


def parsing_coordinate(coord_str):
    """Parses a coordinate string 'x,y,z' into a tuple."""
    try:
        parcing = tuple(coord_str.split(","))
        if len(parcing) != 3:
            raise ValueError("Coordinates must have exactly 3 values")
        x, y, z = [int(i) for i in parcing]
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{coord_str}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")
        return None
    else:
        print(f'Parsing coordinates: "{coord_str}"')
        return (x, y, z)


def main():
    """Main function demonstrating 3D coordinate system."""
    print("=== Game Coordinate System ===\n")

    pos0 = create_3D_position(0, 0, 0)
    pos1 = create_3D_position(10, 20, 5)
    dist = calculate_distance(pos0, pos1)

    print(f"Position created: {pos1}")
    print(f"Distance between {pos0} and {pos1}: {dist:.2f}\n")

    pos2 = parsing_coordinate("3,4,0")
    if pos2 is not None:
        print(f"Parsed position: {pos2}")
        dist = calculate_distance(pos0, pos2)
        print(f"Distance between {pos0} and {pos2}: {dist}\n")

    pos3 = parsing_coordinate("abc,def,ghi")
    if pos3 is not None:
        print(f"Parsed position: {pos3}")
        dist = calculate_distance(pos0, pos2)
        print(f"Distance between {pos0} and {pos3}: {dist}\n")

    if pos2 is not None:
        print("Unpacking demonstration:")
        (x, y, z) = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
