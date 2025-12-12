from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

@dataclass
class Region:
    w: int
    h: int
    counts: list[int]

def parse_shape(s: str) -> list[str]:
    return s.split("\n")[1:]

def parse_region(s: str) -> Region:
    xs = ints(s)
    return Region(xs[0], xs[1], xs[2:])

def totally_fits(r: Region) -> bool:
    area = r.w * r.h
    return sum(r.counts) * 9 <= area

with PuzzleContext(year=2025, day=12) as ctx:

    gs = ctx.groups
    regions = [parse_region(s) for s in gs[-1].split("\n") if s]
    # shapes = list(map(parse_shape, gs[:-1]))
    
    ans = 0
    for r in regions:
        if totally_fits(r):
            ans += 1

    print(ans)
