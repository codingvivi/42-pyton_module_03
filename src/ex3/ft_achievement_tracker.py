import random

ACHIEVEMENTS = (
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
)


class Player:
    def __init__(
        self, name: str, achievements: set[str] | None = None
    ) -> None:
        self.name: str = name.title()

        self.achievements: set[str] = (
            achievements if achievements else gen_player_achievements()
        )

    def show_gotten(self) -> None:
        print(f"{self.name}: {self.achievements}")

    def show_missing(self) -> None:
        missing: set[str] = set(ACHIEVEMENTS) - self.achievements
        print(f"{self.name} is missing: {missing}")

    def show_unique(self, playerbase_rest: tuple["Player", ...]) -> None:
        achievements_rest: set[str] = set().union(
            *(p.achievements for p in playerbase_rest)
        )

        diff: set[str] = self.achievements - achievements_rest
        print(f"Only {self.name} has: {diff}")


def print_header(title: str) -> None:
    print(f"=== {title} ===")


# each player draws between MIN_PICK and MAX_PICK of the achievements
# band is tuned so sets are all likely non-empty in a given run
MIN_PICK = 6
MAX_PICK = 10


def gen_player_achievements() -> set[str]:
    num: int = random.randint(MIN_PICK, MAX_PICK)
    return set(random.sample(ACHIEVEMENTS, num))


def playerbase_show(playerbase: tuple[Player, ...], show_version: str) -> None:
    for p in playerbase:
        # classes are just mapping proxies
        # (read-ony dicts).
        # getattr() does the same thing,
        # but alas, the pdf guidelines,
        method = p.__class__.__dict__[f"show_{show_version}"]
        if show_version == "unique":
            rest = tuple(other for other in playerbase if other is not p)
            method(p, rest)
        else:
            method(p)


def main() -> None:
    print_header("Achievement Tracker System")

    alice: Player = Player("alice")
    bob: Player = Player("bob")
    charlie: Player = Player("charlie")
    dylan: Player = Player("dylan")

    playerbase: tuple[Player, ...] = (alice, bob, charlie, dylan)

    playerbase_show(playerbase, "gotten")
    print("")

    all: set[str] = set().union(
        alice.achievements,
        bob.achievements,
        charlie.achievements,
        dylan.achievements,
    )
    print(f"All distinct achievements: {all}")
    print("")

    common: set[str] = alice.achievements.intersection(
        bob.achievements,
        charlie.achievements,
        dylan.achievements,
    )
    print(f"Common achievements: {common}")
    print("")

    playerbase_show(playerbase, "unique")
    print("")

    playerbase_show(playerbase, "missing")
    print("")


if __name__ == "__main__":
    main()
