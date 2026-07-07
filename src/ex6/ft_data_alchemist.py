import random


def print_header(title: str) -> None:
    print(f"=== {title} ===")


def main() -> None:
    print_header("Game Data Alchemist")

    names_base: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {names_base}")

    names_title: list[str] = [n.capitalize() for n in names_base]
    print(f"New list with all names capitalized: {names_title}")

    names_original: list[str] = [n for n in names_base if n[0].isupper()]
    print(f"New list of capitalized names only: {names_original}")
    print("")

    scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in names_title
    }
    print(f"Score dict: {scores}")

    avg: float = sum(s for s in scores.values()) / len(names_title)
    print(f"Score average is {round(avg, 2)}")

    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > avg
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
