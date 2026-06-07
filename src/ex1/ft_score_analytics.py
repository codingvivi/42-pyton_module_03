import sys


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


def main() -> None:
    print_header("Player Score Analytics")

    args: list[str] = sys.argv[1:]

    scores: list[int] = []
    for arg in args:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            f"No scores provided. Usage: python3 {sys.argv[0]} "
            "<score1> <score2> ...\n"
        )
        return

    print(f"Scores processed: {scores}")

    players: int = len(scores)
    print(f"Total players: {players}")

    total: int = sum(scores)
    print(f"Total score: {total}")

    avrg: float = total / players
    print(f"Average score: {avrg}")

    hi: int = max(scores)
    print(f"High score: {hi}")

    lo: int = min(scores)
    print(f"Low score: {lo}")

    score_range: int = hi - lo
    print(f"Score range: {score_range}\n")


if __name__ == "__main__":
    main()
