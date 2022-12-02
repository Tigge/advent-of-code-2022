def find_largest(carriers):
    return max(map(sum, carriers))


def find_three_largest(carriers):
    sorted_max = sorted(map(sum, carriers), reverse=True)
    return sum(sorted_max[0:3])


def parse(f):
    data = f.read().strip()
    carriers = data.split("\n\n")
    return list(map(lambda c: list(map(lambda n: int(n), c.split("\n"))), carriers))


with open("day1.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))
    print("Part 1:", find_largest(d))
    print("Part 2:", find_three_largest(d))
