def fully_contains(assignment_pairs):
    def contains(p1, p2):
        return p1[0] >= p2[0] and p1[1] <= p2[1]

    return sum(
        [contains(ps[0], ps[1]) or contains(ps[1], ps[0]) for ps in assignment_pairs]
    )


def overlaps(assignment_pairs):
    def overlaps(p1, p2):
        return p1[0] <= p2[1] and p2[0] <= p1[1]

    return sum(
        [overlaps(ps[0], ps[1]) or overlaps(ps[1], ps[0]) for ps in assignment_pairs]
    )


def parse(f):
    return [
        tuple(
            tuple(int(nums) for nums in parts.split("-")) for parts in line.split(",")
        )
        for line in f.readlines()
    ]


with open("day4.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))
    print("Part 1:", fully_contains(d))
    print("Part 2:", overlaps(d))
