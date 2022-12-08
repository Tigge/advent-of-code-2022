def visible(tree_line):
    m = -1
    for tree, c in tree_line:
        if tree > m:
            yield c
            m = tree


def visible_trees(height_map):
    w, h = len(height_map[0]), len(height_map)
    v = set()
    for x, hor_line in enumerate(height_map):
        line = [(tree, (x, y)) for (y, tree) in enumerate(hor_line)]
        v |= set(visible(line))
        v |= set(visible(reversed(line)))

    for y in range(w):
        line = [(height_map[x][y], (x, y)) for x in range(h)]
        v |= set(visible(line))
        v |= set(visible(reversed(line)))

    return len(v)


def score(pos, height_map):
    w, h = len(height_map[0]), len(height_map)
    height = height_map[pos[1]][pos[0]]

    # Right
    x1 = 0
    for x in range(pos[0] + 1, w):
        x1 += 1
        if height_map[pos[1]][x] >= height:
            break
    # Left
    x2 = 0
    for x in range(pos[0] - 1, -1, -1):
        x2 += 1
        if height_map[pos[1]][x] >= height:
            break

    # Down
    y1 = 0
    for y in range(pos[1] + 1, h):
        y1 += 1
        if height_map[y][pos[0]] >= height:
            break
    # Up
    y2 = 0
    for y in range(pos[1] - 1, -1, -1):
        y2 += 1
        if height_map[y][pos[0]] >= height:
            break

    return x1 * x2 * y1 * y2


def highest_scenic_score(height_map):
    w, h = len(height_map[0]), len(height_map)
    s = 0
    for x in range(w):
        for y in range(h):
            s = max(s, score((x, y), height_map))
    return s


def parse(f):
    return [[int(number) for number in line] for line in f.read().strip().split()]


with open("day8.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", visible_trees(d))
    print("Part 2:", highest_scenic_score(d))
