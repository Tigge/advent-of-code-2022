def part1(data):
    return sum([data[1][c - 1] for c in [20, 60, 100, 140, 180, 220]])


def part2(data):
    crt, crt_index = "\n", 0

    for x in data[0]:
        crt += "#" if x - 1 <= crt_index <= x + 1 else "."
        crt_index += 1

        if crt_index == 40:
            crt += "\n"
            crt_index = 0
    return crt


def parse(f):
    data = [line.split() for line in f.read().strip().split("\n")]

    cycle = 1
    reg_x = 1
    reg_x_history = [1]
    signal_strengths = [1]
    for instruction in data:
        if instruction[0] == "addx":
            cycle += 1
            reg_x_history.append(reg_x)
            signal_strengths.append(reg_x * cycle)
            reg_x += int(instruction[1])
            cycle += 1
            reg_x_history.append(reg_x)
            signal_strengths.append(reg_x * cycle)
        if instruction[0] == "noop":
            cycle += 1
            reg_x_history.append(reg_x)
            signal_strengths.append(reg_x * cycle)

    return (reg_x_history, signal_strengths)


with open("day10.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
