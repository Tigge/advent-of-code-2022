import math
import queue
import typing
import re


class DistanceNode(typing.NamedTuple):
    dist: typing.Union[int, float]
    node: str


def dijkstra(vertices: list[str], edges: dict[str, list[str]], source: str):
    dist: dict[str, typing.Union[int, float]] = {source: 0}
    prev: dict[str, typing.Union[str, None]] = {}
    q: queue.PriorityQueue[DistanceNode] = queue.PriorityQueue()
    for v in vertices:
        if v != source:
            dist[v] = math.inf
            prev[v] = None
        q.put(DistanceNode(dist[v], v))

    while not q.empty():
        (_, u) = q.get()
        for v in edges[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                q.put(DistanceNode(alt, v))

    return dist, prev


class Node(typing.NamedTuple):
    flow: int
    edges: list[str]


def nav(
    vertex: str,
    dists: dict[str, dict[str, int]],
    flows: dict[str, int],
    activated: set[str],
    minute: int,
    pressure: int,
    history,
):
    if minute > 30:
        yield (
            pressure,
            activated,
            history,
        )

    # print(activated, "->", vertex)
    minutes_left = 30 - minute
    next_activated = activated.copy()
    next_activated.add(vertex)
    next_pressure = pressure + minutes_left * flows[vertex]
    next_history = history + [(vertex, minute, next_pressure)]

    for vertex_next, minutes in dists[vertex].items():
        # print(vertex_next, minutes)
        # print(vertex_next, minutes)
        if vertex_next == vertex or vertex_next in activated:
            continue

        # if (minutes + 1) > minutes_left:
        #     continue

        yield from nav(
            vertex_next,
            dists,
            flows,
            next_activated,
            minute + minutes + 1,
            next_pressure,
            next_history,
        )


def part1(valves):
    start = "AA"
    # dist: dict[str, dict[str, int]] = {
    #     "AA": {"DD": 1},
    #     "DD": {"BB": 2},
    #     "BB": {"JJ": 3},
    #     "JJ": {"HH": 7},
    #     "HH": {"EE": 3},
    #     "EE": {"CC": 2},
    #     "CC": {},
    # }
    return max(nav(start, valves[1], valves[2], set([start]), 0, 0, []))


def part2(valves):
    pass


def parse(f):
    # return {
    #     match[0]: Node(int(match[1]), match[2].split(", "))
    #     for match in re.findall(
    #         r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z ,]+)",
    #         f.read(),
    #     )
    # }

    vertices: list[str] = []
    edges: dict[str, list[str]] = {}
    dists: dict[str, dict[str, int]] = {}
    flows: dict[str, int] = {}

    for match in re.findall(
        r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z ,]+)",
        f.read(),
    ):
        vertices.append(match[0])
        edges[match[0]] = match[2].split(", ")
        flows[match[0]] = int(match[1])

    for vertex in vertices:
        dists[vertex] = dijkstra(vertices, edges, vertex)[0]

    return vertices, dists, flows


with open("day16.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print(d)

    print("Part 1:", part1(d))
    # print("Part 2:", part2(d))
