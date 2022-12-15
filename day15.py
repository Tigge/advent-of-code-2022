import typing
import re


class Pos2D(typing.NamedTuple):
    x: int
    y: int


class Sensor(typing.NamedTuple):
    pos: Pos2D
    beacon: Pos2D
    range: int


def distance(a: Pos2D, b: Pos2D):
    return abs(a.x - b.x) + abs(a.y - b.y)


def part1(sensors):
    y = 2_000_000
    beacons = set(sensor.beacon for sensor in sensors)
    occupied = set()
    for sensor in sensors:
        y_dist = abs(sensor.pos.y - y)
        leftover_dist = sensor.range - y_dist
        for x in range(sensor.pos.x - leftover_dist, sensor.pos.x + leftover_dist + 1):
            occupied.add(Pos2D(x, y))

    return len(occupied - beacons)


def part2(sensors):
    SIZE = 4_000_000
    y = 0
    while y < SIZE:
        x = 0
        while x < SIZE:
            pos = Pos2D(x, y)
            for sensor in sensors:
                y_dist = abs(sensor.pos.y - pos.y)
                leftover_dist = sensor.range - y_dist

                if leftover_dist < 0:
                    continue

                x_range = (
                    sensor.pos.x - leftover_dist,
                    sensor.pos.x + leftover_dist,
                )

                if x_range[0] <= pos.x <= x_range[1]:
                    x = x_range[1] + 1
                    break
            else:
                return pos.x * 4_000_000 + pos.y
        y += 1


def parse(f):
    positions = [
        Pos2D(int(match[0]), int(match[1]))
        for match in re.findall(r"x=(-?\d+), y=(-?\d+)", f.read())
    ]

    return [
        Sensor(
            positions[i],
            positions[i + 1],
            distance(positions[i], positions[i + 1]),
        )
        for i in range(0, len(positions), 2)
    ]


with open("day15.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
