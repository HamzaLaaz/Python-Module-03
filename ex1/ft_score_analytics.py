import sys

print("=== Player Score Analytics ===")
if len(sys.argv) > 1:
    scores = []
    for i in range(1, len(sys.argv)):
        try:
            arg = int(sys.argv[i])
        except ValueError:
            print("Error: Scores must be numbers!")
        else:
            scores.append(arg)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
else:
    print(f"No scores provided. Usage: python3 {sys.argv[0]} "
          f"<score1> <score2> ...")
