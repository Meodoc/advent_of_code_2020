from enum import Enum, IntEnum


class Cardinal(IntEnum):
    NORTH = 0,
    EAST = 90,
    SOUTH = 180,
    WEST = 270


class Direction(Enum):
    LEFT = 0,
    RIGHT = 1


class Ship:
    def __init__(self):
        self.dir = Cardinal.EAST
        self.position = [0, 0]
        self.waypoint = [10, 1]

    def forward_ship(self, units: int):
        self._move(self.position, self.dir, units)

    def forward_waypoint(self, n: int):
        self.position[0] = self.position[0] + self.waypoint[0] * n
        self.position[1] = self.position[1] + self.waypoint[1] * n

    def move_ship(self, direction: Cardinal, units: int):
        self._move(self.position, direction, units)

    def move_waypoint(self, direction: Cardinal, units: int):
        self._move(self.waypoint, direction, units)

    def turn_ship(self, direction: Direction, degrees: int):
        if direction == Direction.RIGHT:
            self.dir = (self.dir + degrees) % 360
        elif direction == Direction.LEFT:
            self.dir = (self.dir - degrees) % 360
        else:
            raise AttributeError("Turn can only be called with left or right")

    def turn_waypoint(self, direction: Direction, degrees: int):
        if direction == Direction.RIGHT and degrees == 90 or direction == Direction.LEFT and degrees == 270:
            self.waypoint[0], self.waypoint[1] = self.waypoint[1], -self.waypoint[0]
        elif degrees == 180:
            self.waypoint[0], self.waypoint[1] = -self.waypoint[0], -self.waypoint[1]
        elif direction == Direction.RIGHT and degrees == 270 or direction == Direction.LEFT and degrees == 90:
            self.waypoint[0], self.waypoint[1] = -self.waypoint[1], self.waypoint[0]
        else:
            raise AttributeError("Invalid direction or number of degrees")

    def _move(self, entity: list, direction: Cardinal, units: int):
        if direction == Cardinal.NORTH:
            entity[1] += units
        elif direction == Cardinal.EAST:
            entity[0] += units
        elif direction == Cardinal.SOUTH:
            entity[1] -= units
        elif direction == Cardinal.WEST:
            entity[0] -= units
        else:
            raise AttributeError("Move can only be called with cardinal directions")