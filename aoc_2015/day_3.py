"""AOC 2015 - Day 3: Perfectly Spherical Houses in a Vacuum"""

def read_input_line(filename: str) -> str:
    """Reads in AOC puzzle input."""

    with open(filename, 'r') as f:
        input = f.readline()
    
    return input


NORTH = '^'
SOUTH = 'v'
EAST = '>'
WEST = '<'

if __name__ == "__main__":
    

    # input = read_input_line('day_3_input.txt')
    old_coordinate = [0, 0]
    coordinates_visited = [[0, 0]]

    # for direction in input:
    #     if direction == NORTH:
    #         old_coordinate[1] += 1
    #     elif direction == SOUTH:
    #         old_coordinate[1] -= 1
    #     elif direction == EAST:
    #         old_coordinate[0] += 1
    #     elif direction == WEST:
    #         old_coordinate[0] -= 1
        
    #     if old_coordinate.copy() not in coordinates_visited:
    #         coordinates_visited.append(old_coordinate.copy())
    
    # print(len(coordinates_visited))

    input = read_input_line('day_3_input.txt')

    santa_directions = []
    robot_directions = []
    old_coordinate_santa = [0, 0]
    old_coordinate_robot = [0, 0]
    coordinates_visited = [[0, 0]]

    for i, direction in enumerate(input):
        if not i % 2:
            if direction == NORTH:
                old_coordinate_santa[1] += 1
            elif direction == SOUTH:
                old_coordinate_santa[1] -= 1
            elif direction == EAST:
                old_coordinate_santa[0] += 1
            elif direction == WEST:
                old_coordinate_santa[0] -= 1
            
            if old_coordinate_santa.copy() not in coordinates_visited:
                coordinates_visited.append(old_coordinate_santa.copy())
        else: 
            if direction == NORTH:
                old_coordinate_robot[1] += 1
            elif direction == SOUTH:
                old_coordinate_robot[1] -= 1
            elif direction == EAST:
                old_coordinate_robot[0] += 1
            elif direction == WEST:
                old_coordinate_robot[0] -= 1
            
            if old_coordinate_robot.copy() not in coordinates_visited:
                coordinates_visited.append(old_coordinate_robot.copy())
    
    print(coordinates_visited)
    print(len(coordinates_visited))
    

