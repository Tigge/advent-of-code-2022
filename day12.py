import re
import math
import operator
import copy
import queue
import typing


class Pos2D(typing.NamedTuple):
    x: int
    y: int


class DistancePos2D(typing.NamedTuple):
    dist: int | float
    pos: Pos2D


Map2D = dict[Pos2D, int]


NEIGHBOR_OFFSETS: list[Pos2D] = [Pos2D(0, -1), Pos2D(1, 0), Pos2D(0, 1), Pos2D(-1, 0)]


def neighbors_up(source: Pos2D, m: Map2D) -> typing.Iterable[Pos2D]:
    for offset in NEIGHBOR_OFFSETS:
        neighbor = Pos2D(source.x + offset.x, source.y + offset.y)
        if neighbor in m and m[neighbor] - m[source] <= 1:
            yield neighbor


def neighbors_down(source: Pos2D, m: Map2D) -> typing.Iterable[Pos2D]:
    for offset in NEIGHBOR_OFFSETS:
        neighbor = Pos2D(source.x + offset.x, source.y + offset.y)
        if neighbor in m and -1 <= m[neighbor] - m[source]:
            yield neighbor


def dijkstra(
    m: Map2D,
    source: Pos2D,
    neighbors: typing.Callable[[Pos2D, Map2D], typing.Iterable[Pos2D]],
):
    dist: dict[Pos2D, int | float] = {source: 0}
    prev: dict[Pos2D, Pos2D | None] = {}
    q: queue.PriorityQueue[DistancePos2D] = queue.PriorityQueue()
    for v in m:
        if v != source:
            dist[v] = math.inf
            prev[v] = None
        q.put(DistancePos2D(dist[v], v))

    while not q.empty():
        (_, u) = q.get()
        for v in neighbors(u, m):
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                q.put(DistancePos2D(alt, v))

    return dist, prev


def djikstra_path(prev, target: Pos2D) -> list[Pos2D]:
    s: list[Pos2D] = []
    u: Pos2D = target
    while u is not None:
        s.insert(0, u)
        u = prev.get(u, None)
    return s


def part1(m):
    dist, prev = dijkstra(m[0], m[1], neighbors_up)
    return dist[m[2]]


def part2(m):
    dist, prev = dijkstra(m[0], m[2], neighbors_down)
    return min([dist[pos] for pos in m[0] if m[0][pos] == 0])


def parse(f) -> tuple[Map2D, Pos2D, Pos2D]:
    m: Map2D = dict(())
    start: Pos2D | None = None
    end = Pos2D | None
    for y, line in enumerate(f.read().strip().split()):
        for x, char in enumerate(line):
            if char == "S":
                m[(start := Pos2D(x, y))] = ord("a") - 97
            elif char == "E":
                m[(end := Pos2D(x, y))] = ord("z") - 97
            else:
                m[Pos2D(x, y)] = ord(char) - 97

    return (m, start, end)  # type: ignore


with open("day12.txt", "r", encoding="utf-8") as f:
    d = parse(f)

    print("Part 1:", part1(d))
    print("Part 2:", part2(d))
