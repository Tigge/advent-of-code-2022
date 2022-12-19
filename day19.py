import copy
import functools
import itertools
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


def add(a: Resources, b: Resources) -> Resources:
    return tuple(map(operator.add, a, b))


def sub(a: Resources, b: Resources) -> Resources:
    return tuple(map(operator.sub, a, b))


def maxx(a: Resources, b: Resources) -> Resources:
    return tuple(map(max, a, b))


def lt(a: Resources, b: Resources) -> bool:
    return any(map(operator.lt, a, b))


c2 = dict()


def possible_builds(
    blueprint: Blueprint,
    robots: Robots,
    resources_left: Resources,
    built_robots: Robots = (0, 0, 0, 0),
):

    ck = str((blueprint, robots, resources_left, built_robots))
    if ck in c2:
        return c2[ck]

    # print(
    #     "B", blueprint, resources, robots, any(resource < 0 for resource in resources)
    # )

    if robots[1] == 0:
        maxb = functools.reduce(maxx, blueprint.robot_costs[0:2])
    elif robots[2] == 0:
        maxb = functools.reduce(maxx, blueprint.robot_costs[0:3])
    else:
        maxb = functools.reduce(maxx, blueprint.robot_costs)

    # Can't build it
    if lt(resources_left, (0, 0, 0, 0)):
        c2[ck] = []
        return []

    res: list[tuple[Robots, Resources]] = (
        possible_builds(
            blueprint,
            robots,
            sub(resources_left, blueprint.robot_costs[0]),
            add(built_robots, (1, 0, 0, 0)),
        )
        + possible_builds(
            blueprint,
            robots,
            sub(resources_left, blueprint.robot_costs[1]),
            add(built_robots, (0, 1, 0, 0)),
        )
        + possible_builds(
            blueprint,
            robots,
            sub(resources_left, blueprint.robot_costs[2]),
            add(built_robots, (0, 0, 1, 0)),
        )
        + possible_builds(
            blueprint,
            robots,
            sub(resources_left, blueprint.robot_costs[3]),
            add(built_robots, (0, 0, 0, 1)),
        )
    )

    # print(resources, maxb, " : ", robots, blueprint.robot_costs, lt(resources, maxb))
    if lt(resources_left, maxb):
        res += [(built_robots, resources_left)]

    c2[ck] = res

    return res


c = dict()


def execute(
    blueprint: Blueprint,
    step: int = 1,
    robots: Robots = (1, 0, 0, 0),
    resources: Resources = (0, 0, 0, 0),
):
    ck = str((blueprint, step, robots, resources))
    if ck in c:
        return c[ck]

    builds = list(possible_builds(blueprint, robots, resources))
    resources_added = copy.copy(robots)

    # print(
    #     f"Step {step},  resource {resources} -> {add(resources, resources_added)}, robots {robots}"
    # )
    # print("  ", builds)
    # print()

    STEPS = 17

    # if step == STEPS:
    #     print(add(resources, resources_added), robots)

    result = (
        resources[3]
        if step == STEPS
        else max(
            [
                execute(
                    blueprint,
                    step + 1,
                    add(robots, robots_built),
                    add(resources_left, resources_added),
                )
                for robots_built, resources_left in builds
            ]
        )
    )

    c[ck] = result
    return result


def part1(blueprints):
    print(execute(blueprints[0]))
    pass


def part2(cubes):
    pass


def parse(f):
    def parse_blueprint(b):
        return Blueprint(
            int(b[0]),
            [
                (int(b[1]), 0, 0, 0),
                (int(b[2]), 0, 0, 0),
                (int(b[3]), int(b[4]), 0, 0),
                (int(b[5]), 0, int(b[6]), 0),
            ],
        )

    return [
        parse_blueprint(data)
        for data in re.findall(
            r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.",
            f.read(),
        )
    ]


with open("day19.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print(len(d), d)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
