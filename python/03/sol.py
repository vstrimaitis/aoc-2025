from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def solve1(l: str) -> int:
    mx = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            x = int(l[i] + l[j])
            if x > mx:
                mx = x
    return mx

def solve2(s: str) -> int:
    @ft.cache
    def dp(n: int, l: int) -> int:
        if l == 0:
            return 0
        if n < l:
            return -10**100
        return max(
            dp(n-1, l),
            dp(n-1, l-1) * 10 + int(s[n-1])
        )
    return dp(len(s), 12)

with PuzzleContext(year=2025, day=3) as ctx:
    ans1, ans2 = 0, 0

    for l in ctx.lines:
        ans1 += solve1(l)
        ans2 += solve2(l)

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
