import sys


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


def main() -> None:
    print_header("Command Quest")
    print(f"Program name: {sys.argv[0]}")

    args: list[str] = sys.argv[1:]
    i: int = 1

    if not args:
        print("No arguments provided!")
    else:
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments {len(sys.argv)}")


if __name__ == "__main__":
    main()
