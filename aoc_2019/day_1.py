"""Day 1: The Tyranny of the Rocket Equation."""


def get_input_data(filename: str) -> list[int]:
    """Gets input data as list of integers."""

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = [int(num.strip()) for num in f.readlines()]

    except FileNotFoundError as e:
        raise FileNotFoundError(f'File not found: {filename}') from e

    except ValueError as e:
        raise ValueError(f'Error converting data to integers: {e}') from e

    return data


def get_required_fuel(module: int) -> int:
    """Gets fuel required for a given module."""

    return (module // 3) - 2


def solve_part1() -> int:
    """Solves part 1."""

    puzzle_input = get_input_data('day_1_input.txt')

    fuel_required = [get_required_fuel(module) for module in puzzle_input]

    return sum(fuel_required)


def get_required_fuel_recursive(module: int) -> int:
    """Gets fuel required for a given module and its resultant fuel."""

    fuel_amounts = []
    fuel_needed = (module // 3) - 2

    while fuel_needed:
        fuel_amounts.append(fuel_needed)
        fuel_needed = max(0, get_required_fuel(fuel_needed))

    return sum(fuel_amounts)


def solve_part2() -> int:
    """Solves part 2."""

    puzzle_input = get_input_data('day_1_input.txt')

    fuel_required = [get_required_fuel_recursive(
        module) for module in puzzle_input]

    return sum(fuel_required)


def main():
    """Main script logic."""

    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")


if __name__ == "__main__":
    main()
