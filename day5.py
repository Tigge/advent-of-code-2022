import copy


def rearrange_cratemover_9000(data):
    stacks = data[0]
    for n, fr, to in data[1]:
        for i in range(0, n):
            stacks[to].append(stacks[fr].pop())
    return "".join([stack[-1] for stack in stacks])


def rearrange_cratemover_9001(data):
    stacks = data[0]
    for n, fr, to in data[1]:
        stacks[to].extend(stacks[fr][-n:])
        del stacks[fr][-n:]
    return "".join([stack[-1] for stack in stacks])


def parse(f):
    stacks, moves = f.read().split("\n\n")

    def parse_stacks(stacks):
        size = len(stacks[0]) // 4 + 1
        piles = [[] for x in range(size)]
        for x in range(0, size):
            x_off = 1 + x * 4
            for y in range(0, len(stacks) - 1):
                if stacks[y][x_off] != " ":
                    piles[x].insert(0, stacks[y][x_off])
        return piles

    stacks = parse_stacks(stacks.split("\n"))

    def parse_moves(move):
        parts = move.split(" ")
        return (int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1)

    moves = [parse_moves(line) for line in moves.strip().split("\n")]

    return (stacks, moves)


with open("day5.txt", "r", encoding="utf-8") as f:
    d = list(parse(f))

    print("Part 1:", rearrange_cratemover_9000(copy.deepcopy(d)))
    print("Part 2:", rearrange_cratemover_9001(copy.deepcopy(d)))
