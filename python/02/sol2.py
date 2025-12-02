from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def parse_range(s: str) -> tuple[int, int]:
    a, b = s.split("-")
    return int(a), int(b)

def gen(max_parts: int | None, limit: int) -> list[int]:
    ans = []
    def gen_fixed(n: int) -> None:
        i = 1
        while True:
            x = int(str(i) * n)
            if x > limit:
                break
            ans.append(x)
            i += 1
    n = 2
    while True:
        if max_parts is not None and n > max_parts:
            break
        l_prev = len(ans)
        gen_fixed(n)
        if len(ans) == l_prev:
            break
        n += 1
    return list(set(ans))

def count(ranges: list[tuple[int, int]], nums: list[int]) -> int:
    s = 0
    for x in nums:
        for l, r in ranges:
            if l <= x <= r:
                s += x
    return s

with PuzzleContext(year=2025, day=2) as ctx:

    ranges = list(map(parse_range, ctx.data.split(",")))

    mx = max(r for _, r in ranges)
    ans1 = count(ranges, gen(2, mx))
    ans2 = count(ranges, gen(None, mx))

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
