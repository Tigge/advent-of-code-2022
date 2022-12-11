import re
import math
import operator
import copy


def simulate(monkeys, rounds, relief=True):
    inspections = [0] * len(monkeys)
    fac = math.prod([monkey[3] for monkey in monkeys])

    for round in range(rounds):
        for n, monkey in enumerate(monkeys):
            while len(monkey[1]) > 0:
                inspections[n] += 1
                item = monkey[1].pop(0)
                item_n = monkey[2](item)
                if relief:
                    item_n = item_n // 3
                else:
                    item_n = item_n % fac

                if item_n % monkey[3] == 0:
                    monkeys[monkey[4]][1].append(item_n)
                else:
                    monkeys[monkey[5]][1].append(item_n)

    return math.prod(sorted(inspections)[-2:])


def part1(monkeys):
    return simulate(copy.deepcopy(monkeys), 20)


def part2(monkeys):
    return simulate(copy.deepcopy(monkeys), 10000, relief=False)


def parse(f):
    regex = r"Monkey (\d+):\n  Starting items: ([0-9, ]+)\n  Operation: new = ([old +* 0-9]+)\n  Test: divisible by (\d+)\n    If true: throw to monkey (\d+)\n    If false: throw to monkey (\d+)"
    matches = re.finditer(regex, f.read(), re.MULTILINE)

    def parse_operation(operation):
        parts = operation.split()
        oper = operator.add if parts[1] == "+" else operator.mul
        return lambda old: oper(
            old if parts[0] == "old" else int(parts[0]),
            old if parts[2] == "old" else int(parts[2]),
        )

    def parse(match):
        return (
            int(match.group(1)),
            [int(m) for m in match.group(2).split(", ")],
            parse_operation(match.group(3)),
            int(match.group(4)),
            int(match.group(5)),
            int(match.group(6)),
        )

    return [parse(match) for match in matches]


with open("day11.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
