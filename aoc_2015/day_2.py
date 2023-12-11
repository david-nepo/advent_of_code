"""AOC 2015 - Day 2: I Was Told There Would Be No Math"""


def read_input(filename: str) -> str:
    """Reads in AOC puzzle input."""

    with open(filename, 'r') as f:
        input = [line.strip() for line in f.readlines()]

    return input


def split_string(input: str) -> list[str]:
    """Splits string by 'x'."""
    
    return input.split('x')


def convert_to_integers(dim_strings: list[str]) -> list[int]:
    """Converts dimensions to integers."""
    
    return [int(dim) for dim in dim_strings]

    
def calculate_wrapping_paper(dims: list[int]) -> int:
    """Calculates minimum wrapping paper area."""
    
    l, w, h = dims[0], dims[1], dims[2]

    return (2 * l * w) + (2 * w * h) + (2 * h * l)


def get_smallest_area(dims: list[int]) -> int:
    """Returns smallest sided area."""
    
    l, w, h = dims[0], dims[1], dims[2]
    
    return min((l * w), (w * h), (h * l))


def calculate_total_wrapping_paper(input: str) -> int:
    """Calculates total wrapping paper for a gift dimension."""

    input = split_string(input)
    input_dims = convert_to_integers(input)

    return calculate_wrapping_paper(input_dims) + get_smallest_area(input_dims)


def get_smallest_side_perimeter(dims: list[int]) -> int:
    """Calculates smallest perimeter of any one face."""

    sorted_dims = sorted(dims)

    side_a = sorted_dims[0]
    side_b = sorted_dims[1]

    return (2 * side_a) + (2 * side_b)


def calculate_cubic_volume(dims: list[int]) -> int:
    """Calculates cubic feet of volume of a present."""

    l, w, h = dims[0], dims[1], dims[2]

    return l * w * h


def get_total_ribbon_length(input: str) -> int:
    """Gets total length of ribbon required."""

    input = split_string(input)
    input_dims = convert_to_integers(input)

    return get_smallest_side_perimeter(input_dims) + calculate_cubic_volume(input_dims)


if __name__ == "__main__":
    
    gift_sizes = read_input('day_2_input.txt')

    total_paper_required = 0
    total_ribbon_required = 0
    for dimensions in gift_sizes:
        total_paper_required += calculate_total_wrapping_paper(dimensions)
        total_ribbon_required += get_total_ribbon_length(dimensions)

    print(f"Total paper area required: {total_paper_required}")
    print(f"Total ribbon length required: {total_ribbon_required}")
