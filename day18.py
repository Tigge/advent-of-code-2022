import itertools
import typing


class Pos3D(typing.NamedTuple):
    x: int
    y: int
    z: int


class Rect3D(typing.NamedTuple):
    a: Pos3D
    b: Pos3D


def add(a: Pos3D, b: Pos3D):
    return Pos3D(a.x + b.x, a.y + b.y, a.z + b.z)


def inside(a: Pos3D, rect: Rect3D):
    return (
        min(rect.a.x, rect.b.x) <= a.x <= max(rect.a.x, rect.b.x)
        and min(rect.a.y, rect.b.y) <= a.y <= max(rect.a.y, rect.b.y)
        and min(rect.a.z, rect.b.z) <= a.z <= max(rect.a.z, rect.b.z)
    )


DIRS = [Pos3D(*offset) for offset in itertools.product([-1, 0, 1], repeat=3)].remove(
    Pos3D(0, 0, 0)
)
DIRS = [
    Pos3D(0, 0, 1),
    Pos3D(0, 0, -1),
    Pos3D(0, 1, 0),
    Pos3D(0, -1, 0),
    Pos3D(1, 0, 0),
    Pos3D(-1, 0, 0),
]


def flood_fill(cubes):
    surface_area = 0
    water_cubes = set()

    bounds = Rect3D(
        Pos3D(
            min(cube.x for cube in cubes) - 1,
            min(cube.y for cube in cubes) - 1,
            min(cube.z for cube in cubes) - 1,
        ),
        Pos3D(
            max(cube.x for cube in cubes) + 1,
            max(cube.y for cube in cubes) + 1,
            max(cube.z for cube in cubes) + 1,
        ),
    )

    q = [bounds.a]

    while len(q) > 0:
        n = q.pop(0)

        if n in cubes:
            surface_area += 1
            continue

        if not inside(n, bounds):
            continue
        elif n in water_cubes:
            continue

        water_cubes.add(n)

        if n in cubes:
            print(n)
            surface_area += 1
        else:
            for neighbours in DIRS:
                q.append(add(n, neighbours))
    return surface_area


def part1(cubes):
    return sum(
        len([neighbor for neighbor in DIRS if add(cube, neighbor) not in cubes])
        for cube in cubes
    )


def part2(cubes):
    return flood_fill(cubes)


def parse(f):
    return set(
        Pos3D(*(int(num) for num in line.split(",")))
        for line in f.read().strip().split("\n")
    )


with open("day18.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
