from src.problem import Problem
from src.day12.ship import Cardinal, Direction, Ship


INSTRUCTIONS_A = {"N": lambda u, ship: ship.move_ship(Cardinal.NORTH, u),
                  "S": lambda u, ship: ship.move_ship(Cardinal.SOUTH, u),
                  "E": lambda u, ship: ship.move_ship(Cardinal.EAST, u),
                  "W": lambda u, ship: ship.move_ship(Cardinal.WEST, u),
                  "L": lambda d, ship: ship.turn_ship(Direction.LEFT, d),
                  "R": lambda d, ship: ship.turn_ship(Direction.RIGHT, d),
                  "F": lambda u, ship: ship.forward_ship(u)}


INSTRUCTIONS_B = {"N": lambda u, ship: ship.move_waypoint(Cardinal.NORTH, u),
                  "S": lambda u, ship: ship.move_waypoint(Cardinal.SOUTH, u),
                  "E": lambda u, ship: ship.move_waypoint(Cardinal.EAST, u),
                  "W": lambda u, ship: ship.move_waypoint(Cardinal.WEST, u),
                  "L": lambda d, ship: ship.turn_waypoint(Direction.LEFT, d),
                  "R": lambda d, ship: ship.turn_waypoint(Direction.RIGHT, d),
                  "F": lambda u, ship: ship.forward_waypoint(u)}


def part_a():
    ship = Ship()
    for instr, param in data:
        INSTRUCTIONS_A[instr](param, ship)
    return abs(ship.position[0]) + abs(ship.position[1])


def part_b():
    ship = Ship()
    for instr, param in data:
        INSTRUCTIONS_B[instr](param, ship)
    return abs(ship.position[0]) + abs(ship.position[1])


def load():
    return [(i[0], int(i[1:])) for i in problem.data()]


if __name__ == '__main__':
    problem = Problem(12)
    data = load()

    problem.submit(part_a(), 'a')  # 1032
    problem.submit(part_b(), 'b')  # 156735
