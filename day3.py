def get_priority(item):
    if ord("A") <= ord(item) <= ord("Z"):
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1


def misplaced_priority(rucksacks):
    return sum(map(lambda r: get_priority(list(r[0] & r[1])[0]), rucksacks))


def badge_priority(rucksacks):
    s = 0
    for i in range(0, len(rucksacks), 3):
        item = list(
            (rucksacks[i + 0][0] | rucksacks[i + 0][1])
            & (rucksacks[i + 1][0] | rucksacks[i + 1][1])
            & (rucksacks[i + 2][0] | rucksacks[i + 2][1])
        )[0]
        s += get_priority(item)
    return s


def parse(f):
    rucksacks = list(map(lambda line: line.strip(), f.readlines()))
    return map(lambda r: (set(r[: (len(r) // 2)]), set(r[(len(r) // 2) :])), rucksacks)


with open("day3.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))
    print("Part 1:", misplaced_priority(d))
    print("Part 2:", badge_priority(d))
