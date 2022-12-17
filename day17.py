import itertools


WIDTH = 7

PIECES = [
    [["@", "@", "@", "@"]],
    [[" ", "@", " "], ["@", "@", "@"], [" ", "@", " "]],
    [["@", "@", "@"], [" ", " ", "@"], [" ", " ", "@"]],
    [["@"], ["@"], ["@"], ["@"]],
    [["@", "@"], ["@", "@"]],
]


def overlaps(m, piece, x, y):
    if y < 0:
        return True

    for py, piece_line in enumerate(PIECES[piece]):
        if y + py >= len(m):
            continue
        for px, piece_char in enumerate(piece_line):
            if m[y + py][x + px] == "#" and piece_char == "@":
                return True
    return False


def add_piece_to_map(m, piece, px, py):
    for y in range(0, len(PIECES[piece])):
        while py + y >= len(m):
            m.append(list("." * WIDTH))
        for x in range(0, len(PIECES[piece][0])):
            if PIECES[piece][y][x] == "@":
                m[py + y][px + x] = "#"


# Real

ROCKS_PER_CYCLE = 1700
HEIGHT_PER_CYCLE = 2654
INSTRUCTION_START = 3910
PIECE_START = 1


def tetris(jets: "list[str]", amount_of_rocks: int) -> int:
    rock = 1
    current_piece = 0
    skipped_height = 0
    y = 3
    x = 2

    m = []

    for n, jet in itertools.cycle(enumerate(jets)):

        if jet == "<":
            n_x = max(0, x - 1)
            if not overlaps(m, current_piece, n_x, y):
                x = n_x
        elif jet == ">":
            n_x = min(WIDTH - len(PIECES[current_piece][0]), x + 1)
            if not overlaps(m, current_piece, n_x, y):
                x = n_x

        if overlaps(m, current_piece, x, y - 1):

            add_piece_to_map(m, current_piece, x, y)

            if n == INSTRUCTION_START and current_piece == PIECE_START:
                cycles = (amount_of_rocks - rock) // ROCKS_PER_CYCLE
                rock += cycles * ROCKS_PER_CYCLE
                skipped_height = cycles * HEIGHT_PER_CYCLE

            if rock == amount_of_rocks:
                return len(m) + skipped_height

            current_piece = (current_piece + 1) % len(PIECES)
            x, y = 2, len(m) + 3
            rock += 1

        else:
            y -= 1


def part1(jets):
    return tetris(jets, 2022)


def part2(jets):
    return tetris(jets, 1_000_000_000_000)


def parse(f):
    return f.read().strip()


with open("day17.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
