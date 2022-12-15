import copy
import itertools
import typing
import re


class Pos2D(typing.NamedTuple):
    x: int
    y: int


def distance(a: Pos2D, b: Pos2D):
    return abs(a.x - b.x) + abs(a.y - b.y)


def part1(data):
    # print(data)
    # y = 10
    y = 2000000
    occupied = set()
    beacons = set(b[1] for b in data[2])
    # for x in range(data[0].x - 20, data[1].x + 20):
    #     # print(x)
    #     p = Pos2D(x, y)
    #     for sensor in data[2]:
    #         # print(sensor)
    #         if distance(sensor[0], p) <= distance(sensor[0], sensor[1]):
    #             # print(
    #             #     p,
    #             #     " in range of ",
    #             #     (sensor[0], sensor[1]),
    #             #     distance(sensor[0], sensor[1]),
    #             # )
    #             if p not in beacons:
    #                 occupied.append(p)
    #                 break

    # print(occupied)
    # return len(occupied)
    # pass
    occupied = set()
    for sensor in data[2]:
        s_range = distance(sensor[0], sensor[1])
        y_dist = abs(sensor[0].y - y)
        x_left = s_range - y_dist

        print("sensor", sensor[0], s_range, s_range - y_dist + 1)

        for x in range(sensor[0].x - x_left, sensor[0].x + x_left + 1):
            # print(x)
            occupied.add(Pos2D(x, y))

    # 24065393

    return len(occupied - beacons)


def part2(data):
    y = 2000000
    beacons = set(b[1] for b in data[2])
    occupied = set()
    for sensor in data[2]:
        s_range = distance(sensor[0], sensor[1])
        y_dist = abs(sensor[0].y - y)
        x_left = s_range - y_dist

        print("sensor", sensor[0], s_range, s_range - y_dist + 1)

        for x in range(
            max(0, sensor[0].x - x_left), min(4000000, sensor[0].x + x_left + 1)
        ):
            # print(x)
            occupied.add(Pos2D(x, y))

    # 24065393

    return len(occupied - beacons)


def parse(f):
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    positions = [
        Pos2D(int(match[0]), int(match[1]))
        for match in re.findall(r"x=(-?\d+), y=(-?\d+)", f.read())
    ]

    small = Pos2D(min([p.x for p in positions]), min([p.y for p in positions]))
    large = Pos2D(max([p.x for p in positions]), max([p.y for p in positions]))

    # print(small, large)

    return (
        small,
        large,
        [tuple(positions[i : i + 2]) for i in range(0, len(positions), 2)],
    )


with open("day15.txt", "r", encoding="utf-8") as f:
    d = parse(f)
    # print(d)

    # print("Part 1:", part1(copy.deepcopy(d)))
    print("Part 2:", part2(copy.deepcopy(d)))
