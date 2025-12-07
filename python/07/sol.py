from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft


with PuzzleContext(year=2025, day=7) as ctx:
    g, n, m = to_grid(ctx.data)
    start_col = ctx.lines[0].index("S")

    ans1 = 0
    counts = [[0]*m for _ in range(n)]
    counts[0][start_col] = 1
    for i in range(n-1):
        for j in range(m):
            if g[i][j] in "S.":
                counts[i+1][j] += counts[i][j]
            if g[i][j] == "^":
                if counts[i][j] > 0:
                    ans1 += 1
                counts[i+1][j-1] += counts[i][j]
                counts[i+1][j+1] += counts[i][j]

    ans2 = sum(counts[-1])
    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
