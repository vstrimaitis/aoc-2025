from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def iter(g: List[List[str]], n: int, m: int) -> tuple[list[list[str]], int]:
    gg = [[g[i][j] for j in range(m)] for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "@" and sum([1 for x in get_neighs(g, i, j, DIRS_8) if x == '@']) < 4:
                gg[i][j] = "."
                cnt += 1
            else:
                gg[i][j] = g[i][j]
    return gg, cnt

with PuzzleContext(year=2025, day=4) as ctx:
    g, n, m = to_grid(ctx.data)

    _, ans1 = iter(g, n, m)

    ans2 = 0
    while True:
        g, cnt = iter(g, n, m)
        ans2 += cnt
        if cnt == 0:
            break
                
    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
