import sys


def main():
    """
    Command Quest - demonstrates how to receive
    and process command line arguments using sys.argv.
    """
    print("=== Command Quest ===")
    if len(sys.argv) > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"No arguments provided!\nProgram name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
