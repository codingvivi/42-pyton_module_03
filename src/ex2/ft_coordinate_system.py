import math

X, Y, Z = 0, 1, 2


def print_header(title: str) -> None:
    print(f"=== {title} ===")


def get_distance_3d(
    pt_1: tuple[float, float, float], pt_2: tuple[float, float, float]
) -> float:

    distance: float = math.sqrt(
        (pt_1[X] - pt_2[X]) ** 2
        + (pt_1[Y] - pt_2[Y]) ** 2
        + (pt_1[Z] - pt_2[Z]) ** 2
    )

    return distance


def get_player_pos() -> tuple[float, float, float]:
    info_msg: str = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        ui_parts: list[str] = input(info_msg).split(",")
        if len(ui_parts) != 3:
            print("Invalid syntax")
            continue

        p: str = ""
        try:
            for p in ui_parts:
                float(p)
            return (float(ui_parts[X]), float(ui_parts[Y]), float(ui_parts[Z]))
        except ValueError as e:
            print(f"Error on parameter '{p.strip()}': {e}")


def main() -> None:
    print_header("Game Coordinate System")

    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[X]}, Y={first[Y]}, Z={first[Z]}")

    origin: tuple[float, float, float] = (0, 0, 0)
    first2origin: float = get_distance_3d(first, origin)
    print(f"Distance to center: {first2origin:.4f}")

    print("")
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    first2second: float = get_distance_3d(first, second)
    print(f"Distance between the 2 sets of coordinates: {first2second:.4f}")


if __name__ == "__main__":
    main()
