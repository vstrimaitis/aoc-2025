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

def solve2(l: str) -> int:
    @ft.cache
    def dp(i: int, ln: int) -> int:
        if i < 0:
            return -10**100
        if ln == 1:
            return int(max(l[:i+1]))
        res = max(
            dp(i-1, ln),
            dp(i-1, ln-1) * 10 + int(l[i])
        )
        return res
    return dp(len(l)-1, 12)
    

with PuzzleContext(year=2025, day=3) as ctx:
    ans1, ans2 = 0, 0

    for l in ctx.lines:
        ans1 += solve1(l)
        ans2 += solve2(l)

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
