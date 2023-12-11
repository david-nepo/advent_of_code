"""AOC 2015 - Day 1: Not Quite Lisp."""

UP = '('
DOWN = ')'


def read_input(filename: str) -> str:
    """Reads in AOC puzzle input."""

    with open(filename, 'r') as f:
        input = f.readline()
    
    return input



def count_floor_movement(instructions: str) -> int:
    """Count net floor movement."""

    return instructions.count(UP) - instructions.count(DOWN)


def get_position_of_basement_instruction(instructions: str) -> int:
    """Gets position of the first character that causes him to enter the basement."""

    counter = 0
    for i, instruction in enumerate(instructions):
        
        counter += 1 if instruction == UP else -1

        if counter == -1:
            return i + 1


if __name__ == "__main__":
    
    print(count_floor_movement(')())())'))

    input = read_input('day_1_input.txt')
    print(count_floor_movement(input))

    print(get_position_of_basement_instruction(input))



    