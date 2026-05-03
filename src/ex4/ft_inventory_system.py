import sys


def print_header(title: str) -> None:
    print(f"=== {title} ===")
    print("")


ITEM = 0
NUM = 1


def inventory_from_cli() -> dict[str, int]:

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        try:
            curr: list = arg.split(":")
            if len(curr) == 1:
                raise ValueError(f"Error - invalid parameter {curr[ITEM]}")
            if len(curr) > 2:
                raise ValueError(f"Error - Too many paramters after {curr[ITEM]}")
            if curr[ITEM] in inventory:
                raise ValueError(f"Error - redundant parameter {curr[ITEM]}")

            try:
                num: int = int(curr[NUM])
                if num < 1:
                    raise ValueError("Item number can't be smaller than 1!")
                inventory[curr[ITEM]] = num
            except ValueError as e:
                print(f"Quantity error for {curr[ITEM]}: {e}")

        except Exception as e:
            print(e)

    return inventory


def main() -> None:
    print_header("Inventory System Analysis")

    inventory: dict[str, int] = inventory_from_cli()

    print(f"Got inventory: {inventory}\n")

    items: list[str] = list(inventory.keys())
    print(f"Item list: {items}\n")

    num_items: int = len(items)
    total_items: int = sum(list(inventory.values()))
    print(f"Total quantity of the {num_items} items: {total_items}\n")

    if total_items:
        max_item: None | str = None
        min_item: None | str = None

        max_num: None | int = None
        min_num: None | int = None

        for item in inventory:
            num: int = inventory[item]
            percent: float = num / total_items * 100
            print(f"Item {item} represents {round(percent, 1)}%")

            if max_num is None or num > max_num:
                max_num = num
                max_item = item

            if min_num is None or num < min_num:
                min_num = num
                min_item = item
        print("")

        print(f"Item most abundant: {max_item} with quantity {max_num}")
        print(f"Item least abundant: {min_item} with quantity {min_num}")
        print("")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
