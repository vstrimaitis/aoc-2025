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

def is_valid(x: int) -> bool:
    s = str(x)
    if len(s) % 2 != 0:
        return True
    n = len(s)
    if s[:n//2] == s[n//2:]:
        return False
    return True

def is_valid_2(x: int) -> bool:
    s = str(x)
    for l in range(1, len(s)):
        if len(s) % l != 0:
            continue
        parts = set()
        for i in range(0, len(s), l):
            parts.add(s[i:i+l])
        if len(parts) == 1:
            return False
    return True

with PuzzleContext(year=2025, day=2) as ctx:
    ans1, ans2 = 0, 0

    ranges = list(map(parse_range, ctx.data.split(",")))

    for l, r in ranges:
        for x in range(l, r+1):
            if not is_valid(x):
                ans1 += x
            if not is_valid_2(x):
                ans2 += x

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
