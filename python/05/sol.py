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

def intersects(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return not (a[1] < b[0] or b[1] < a[0])

def merge(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    assert intersects(a, b)
    return min(a[0], b[0]), max(a[1], b[1])

with PuzzleContext(year=2025, day=5) as ctx:
    a, b = ctx.groups
    ranges = [parse_range(s) for s in a.split()]
    nums = list(map(int, b.split()))

    ans1 = 0
    for x in nums:
        for l, r in ranges:
            if l <= x <= r:
                ans1 += 1
                break

    ctx.submit(1, str(ans1) if ans1 else None)

    while True:
        cont = False
        for i,a in enumerate(ranges):
            for j, b in enumerate(ranges):
                if i < j and intersects(a, b):
                    ranges[i] = merge(a, b)
                    del ranges[j]
                    cont = True
                    break
            if cont:
                break
        if not cont:
            break
    
    ans2 = 0
    for l, r in ranges:
        ans2 += r-l+1

    ctx.submit(2, str(ans2) if ans2 else None)
