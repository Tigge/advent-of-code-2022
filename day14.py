import copy
import itertools
import typing


class Pos2D(typing.NamedTuple):
    x: int
    y: int


Map2D = dict[Pos2D, str]


def simulate(m: Map2D, abyss: int, floor: bool = False):
    for n in itertools.count(1):
        x, y = 500, 0
        for y in range(y, abyss + 2):
            if Pos2D(x, y) in m:
                return n - 1
            elif Pos2D(x, y + 1) not in m:
                continue
            elif Pos2D(x - 1, y + 1) not in m:
                x -= 1
                continue
            elif Pos2D(x + 1, y + 1) not in m:
                x += 1
                continue
            else:
                m[Pos2D(x, y)] = "o"
                break
        else:
            if floor == False:
                return n - 1
            else:
                m[Pos2D(x, y)] = "o"


def part1(data):
    return simulate(*data)


def part2(data):
    return simulate(*data, floor=True)


def parse(f):
    m: Map2D = dict()
    abyss = 0

    for path in [
        [Pos2D(*[int(num) for num in coord.split(",")]) for coord in path.split(" -> ")]
        for path in f.read().strip().split("\n")
    ]:
        for (fr, to) in zip(path, path[1:]):
            abyss = max(abyss, fr.y, to.y)
            for y in range(min(fr.y, to.y), max(fr.y, to.y) + 1):
                for x in range(min(fr.x, to.x), max(fr.x, to.x) + 1):
                    m[Pos2D(x, y)] = "#"

    return m, abyss


with open("day14.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(copy.deepcopy(d)))
    print("Part 2:", part2(copy.deepcopy(d)))
