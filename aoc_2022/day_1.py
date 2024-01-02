"""Day 1: Calorie Counting."""


def get_input_as_list(filename: str) -> list[int | str]:
    """Gets list of all calories."""

    with open(filename, 'r', encoding='utf-8') as f:
        data = [int(row) if row else '-' for row in f.read().split('\n')]

        return data


def convert_input_to_list_of_lists(input_data: list[int | str]) -> list[list[int]]:
    """Converts input data to list of list of integers."""

    calorie_block = []
    result = []

    for calorie_count in input_data:
        if isinstance(calorie_count, int):
            calorie_block.append(calorie_count)

        else:
            result.append(calorie_block)
            calorie_block = []

    if calorie_block:
        result.append(calorie_block)

    return result


def sum_calories_of_each_elf(calorie_list: list[list[int]]) -> list[int]:
    """Sum each elf's calories."""

    return list(map(lambda x: sum(x), calorie_list))


def get_index_of_max_calories(calorie_sums: list[int]) -> int:
    """Gets the index of elf with the most calories."""

    return calorie_sums.index(max(calorie_sums))


def solve_part1():
    """Solves part 1."""

    input_calories = get_input_as_list('inputs_day_1.txt')
    input_calories = convert_input_to_list_of_lists(input_calories)

    elf_calorie_sums = sum_calories_of_each_elf(input_calories)

    return max(elf_calorie_sums)


def solve_part2():
    """Solves part 2."""

    input_calories = get_input_as_list('inputs_day_1.txt')
    input_calories = convert_input_to_list_of_lists(input_calories)

    elf_calorie_sums = sum_calories_of_each_elf(input_calories)

    return sum(sorted(elf_calorie_sums)[-3:])


def main():
    """Main script logic."""

    print(f'Part 1: {solve_part1()}')
    print(f'Part 2: {solve_part2()}')


if __name__ == "__main__":
    main()
