import functools
import operator
import typing
import re

Resources = tuple[int, int, int, int]
Robots = tuple[int, int, int, int]


class RobotCost(typing.NamedTuple):
    ore: int
    clay: int
    obsidian: int


class Blueprint(typing.NamedTuple):
    id: int
    robot_costs: list[Resources]
    robot_max: Robots


def add(a: Resources, b: Resources) -> Resources:
    return tuple(map(operator.add, a, b))


def sub(a: Resources, b: Resources) -> Resources:
    return tuple(map(operator.sub, a, b))


def maxx(a: Resources, b: Resources) -> Resources:
    return tuple(map(max, a, b))


def eq(a: Resources, b: Resources) -> bool:
    return all(map(operator.le, a, b))


def le(a: Resources, b: Resources) -> bool:
    return all(map(operator.le, a, b))


def ge(a: Resources, b: Resources) -> bool:
    return all(map(operator.ge, a, b))


BUILDS = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
]

REQUIREMENTS = [(1, 0, 0, 0), (1, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0)]


def steps_to_build(
    blueprint: Blueprint,
    step: int,
    robots: Robots,
    resources: Resources,
    robot: int,
    max_steps=24,
):
    if not ge(robots, REQUIREMENTS[robot]):
        return None

    # Wait until we can afford a robot (or steps run out)
    while not ge(
        resources,
        blueprint.robot_costs[robot],
    ):
        resources = add(resources, robots)
        step += 1
        if step > max_steps:
            return (step, robots, resources)

    # Build:
    return (
        step + 1,
        add(robots, BUILDS[robot]),
        sub(add(resources, robots), blueprint.robot_costs[robot]),
    )


def execute(
    blueprint: Blueprint,
    step: int = 1,
    robots: Robots = (1, 0, 0, 0),
    resources: Resources = (0, 0, 0, 0),
    max_steps=24,
):
    if step > max_steps:
        return (resources[3], step, robots, resources)

    results = []
    for robot in range(4):
        if robot != 3 and robots[robot] > blueprint.robot_max[robot]:
            continue
        next_step = steps_to_build(blueprint, step, robots, resources, robot, max_steps)
        if next_step is not None:
            results.append(execute(blueprint, *next_step, max_steps))

    return max(results)


def part1(blueprints):
    s = 0
    for blueprint in blueprints:
        a = blueprint.id * execute(blueprint, max_steps=24)[0]
        s += a
        print(blueprint.id, a)
    return s


def part2(blueprints):
    s = 1
    for blueprint in blueprints[0:3]:
        a = blueprint.id * execute(blueprint, max_steps=32)[0]
        s *= a
        print(blueprint.id, a)
    return s


def parse(f):
    def parse_blueprint(b):
        costs: list[Resources] = [
            (int(b[1]), 0, 0, 0),
            (int(b[2]), 0, 0, 0),
            (int(b[3]), int(b[4]), 0, 0),
            (int(b[5]), 0, int(b[6]), 0),
        ]
        return Blueprint(int(b[0]), costs, functools.reduce(maxx, costs))

    return [
        parse_blueprint(data)
        for data in re.findall(
            r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.",
            f.read(),
        )
    ]


with open("day19.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
