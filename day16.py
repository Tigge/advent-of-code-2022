import re


def nav(
    vertex: str,
    dists: dict[str, dict[str, int]],
    flows: dict[str, int],
    activated: set[str],
    minute: int = 0,
    pressure: int = 0,
    max_minutes: int = 0,
):
    minutes_left = max_minutes - minute
    next_activated = activated.copy()
    next_activated.add(vertex)
    next_pressure = pressure + minutes_left * flows[vertex]

    yield (
        next_pressure,
        next_activated,
    )

    for vertex_next, minutes in dists[vertex].items():
        if vertex_next == vertex or vertex_next in next_activated:
            continue

        if (minutes + 1) > minutes_left:
            continue

        yield from nav(
            vertex_next,
            dists,
            flows,
            next_activated,
            minute + minutes + 1,
            next_pressure,
            max_minutes=max_minutes,
        )


def part1(valves):
    return max(nav("AA", valves[1], valves[2], set(["AA"]), max_minutes=30))[0]


def part2(valves):
    pressures = []
    things = list(nav("AA", valves[1], valves[2], set(["AA"]), max_minutes=26))
    for n, (pressure, activated) in enumerate(things):
        elephant_pressure, _ = max(
            nav("AA", valves[1], valves[2], activated, max_minutes=26)
        )
        pressures.append(pressure + elephant_pressure)
    return max(pressures)


def bfs(vertex: str, edges, flows):
    q: list[tuple[str, int]] = [(vertex, 0)]
    explored = set([vertex])

    while len(q) > 0:
        v, l = q.pop(0)
        if v != vertex and flows[v] > 0:
            explored.add(v)
            yield (v, l)

        for w in edges[v]:
            if w not in explored:
                explored.add(w)
                q.append((w, l + 1))


def parse(f):
    vertices: list[str] = []
    edges: dict[str, list[str]] = {}
    flows: dict[str, int] = {}

    for match in re.findall(
        r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z ,]+)",
        f.read(),
    ):
        vertices.append(match[0])
        edges[match[0]] = match[2].split(", ")
        flows[match[0]] = int(match[1])

    vertices: list[str] = [
        vertex for vertex in vertices if flows[vertex] > 0 or vertex == "AA"
    ]
    dists: dict[str, dict[str, int]] = dict(
        (vertex, dict(bfs(vertex, edges, flows))) for vertex in vertices
    )

    return vertices, dists, flows


with open("day16.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
