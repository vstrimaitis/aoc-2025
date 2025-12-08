from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

class DSU:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.sz = [1] * n
    
    def find(self, a: int) -> int:
        if self.par[a] == a:
            return a
        self.par[a] = self.find(self.par[a])
        return self.par[a]

    def unite(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.par[b] = a
        self.sz[a] += self.sz[b]
        return True

    def groups(self) -> list[list[int]]:
        res = defaultdict(list)
        for i in range(len(self.par)):
            res[self.find(i)].append(i)
        return list(res.values())


def d2(a: list[int], b: list[int]) -> int:
    return sum((x - y) ** 2 for x, y in zip(a, b))

with PuzzleContext(year=2025, day=8) as ctx:
    if ctx._is_running_on_sample():
        NEED = 10
    else:
        NEED = 1000

    coords = [ints(l) for l in ctx.lines]
    edges = []
    for i, c1 in enumerate(coords):
        for j, c2 in enumerate(coords):
            if i < j:
                edges.append((i, j, d2(c1, c2)))
    
    dsu = DSU(len(coords))
    edges = sorted(edges, key=lambda x: x[2])
    left = NEED
    cont = -1
    for idx, (i, j, _) in enumerate(edges):
        if left == 0:
            break
        dsu.unite(i, j)
        left -= 1
        cont = idx+1

    groups = sorted(dsu.groups(), key=lambda x: len(x), reverse=True)
    ans1 = 1
    for g in groups[:3]:
        ans1 *= len(g)

    ctx.submit(1, str(ans1) if ans1 else None)

    ans2 = None
    while len(dsu.groups()) > 1:
        i, j, _ = edges[cont]
        dsu.unite(i, j)
        ans2 = coords[i][0] * coords[j][0]
        cont += 1


    ctx.submit(2, str(ans2) if ans2 else None)
