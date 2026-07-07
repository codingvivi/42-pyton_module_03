import random
import typing

NAME = 0
ACTION = 1


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.actions: tuple[str, ...] = (
            "run",
            "eat",
            "sleep",
            "grab",
            "release",
            "move",
            "climb",
            "swim",
            "use",
        )

    def do_action(self, draw: int) -> tuple[str, str]:

        record: tuple[str, str] = (self.name, self.actions[draw])
        return record


def gen_event(
    playerbase: list[Player],
) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        draw: int = random.randrange(len(playerbase))
        player: Player = playerbase[draw]

        draw = random.randrange(len(player.actions))
        yield player.do_action(draw)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        draw: int = random.randrange(len(events))
        yield events.pop(draw)


def print_header(title: str) -> None:
    print(f"=== {title} ===")


def main() -> None:
    print_header("Game Data Stream Processor")
    alice: Player = Player("alice")
    bob: Player = Player("bob")
    charlie: Player = Player("charlie")
    dylan: Player = Player("dylan")

    playerbase: list[Player] = [alice, dylan, bob, charlie]
    gen: typing.Generator[tuple[str, str], None, None] = gen_event(playerbase)

    event: tuple[str, str]
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[NAME]} did action {event[ACTION]}")

    events: list[tuple[str, str]] = [next(gen) for _ in range(10)]
    print(f"Built list of {len(events)} events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
