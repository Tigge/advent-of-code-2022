import math


def sign(v):
    return (v > 0) - (v < 0)


def touching(p1, p2):
    return math.fabs(p1[0] - p2[0]) <= 1 and math.fabs(p1[1] - p2[1]) <= 1


def simulate_rope(data, length=2):
    ks = [(0, 0) for _ in range(length)]
    v = set()
    n = 0
    for move in data:
        for _ in range(move[1]):
            if move[0] == "U":
                ks[0] = (ks[0][0], ks[0][1] - 1)
            elif move[0] == "R":
                ks[0] = (ks[0][0] + 1, ks[0][1])
            elif move[0] == "D":
                ks[0] = (ks[0][0], ks[0][1] + 1)
            elif move[0] == "L":
                ks[0] = (ks[0][0] - 1, ks[0][1])

            for k in range(0, length - 1):
                dx = sign(ks[k][0] - ks[k + 1][0])
                dy = sign(ks[k][1] - ks[k + 1][1])
                if not touching(ks[k], ks[k + 1]):
                    ks[k + 1] = (ks[k + 1][0] + dx, ks[k + 1][1] + dy)

            v.add(ks[-1])

    return len(v)


def part1(data):
    return simulate_rope(data, 2)


def part2(data):
    return simulate_rope(data, 10)


def parse(f):
    return [
        (line.split()[0], int(line.split()[1])) for line in f.read().strip().split("\n")
    ]


with open("day9.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
