import json
import functools


def compare(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return True
        elif left > right:
            return False
        return None

    if type(left) is list and type(right) is list:
        if len(left) == 0 and len(right) > 0:
            return True
        if len(left) > 0 and len(right) == 0:
            return False
        if len(left) == 0 and len(right) == 0:
            return None

        if (val := compare(left[0], right[0])) is not None:
            return val

        return compare(left[1:], right[1:])

    if type(left) is int and type(right) is list:
        return compare([left], right)
    if type(left) is list and type(right) is int:
        return compare(left, [right])


def part1(data):
    right_order = []
    for n, (left, right) in enumerate(data, start=1):
        if compare(left, right):
            right_order.append(n)
    return sum(right_order)


def part2(data):
    packets = sorted(
        [packet for pair in data for packet in pair] + [[[2]], [[6]]],
        key=functools.cmp_to_key(lambda a, b: -int(compare(a, b))),
    )
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def parse(f):
    return [
        tuple(json.loads(line) for line in part.split("\n"))
        for part in f.read().strip().split("\n\n")
    ]


with open("day13.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
