from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def build_segments(coords: list[tuple[int, int]]) -> list[list[tuple[int,int]]]:
    segments = []
    for (x1, y1), (x2, y2) in zip(coords, coords[1:] + [coords[0]]):
        segments.append([(x1, y1), (x2, y2)])
    return segments

def to_rect_inner(x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
    return [
        (min(x1, x2)+1, min(y1, y2)+1),
        (min(x1, x2)+1, max(y1, y2)-1),
        (max(x1, x2)-1, min(y1, y2)+1),
        (max(x1, x2)-1, max(y1, y2)-1),
    ]

def intersects(a: list[tuple[int,int]], b: list[tuple[int,int]]) -> bool:
    a_min_x = min(p[0] for p in a)
    a_max_x = max(p[0] for p in a)
    a_min_y = min(p[1] for p in a)
    a_max_y = max(p[1] for p in a)
    b_min_x = min(p[0] for p in b)
    b_max_x = max(p[0] for p in b)
    b_min_y = min(p[1] for p in b)
    b_max_y = max(p[1] for p in b)
    if a_max_x < b_min_x or b_max_x < a_min_x:
        return False
    if a_max_y < b_min_y or b_max_y < a_min_y:
        return False
    return True

with PuzzleContext(year=2025, day=9) as ctx:
    coords = [ints(l) for l in ctx.lines]

    ans1 = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            dx = abs(x2-x1) + 1
            dy = abs(y2-y1) + 1
            a = abs(dx) * abs(dy)
            ans1 = max(ans1, a)

    ctx.submit(1, str(ans1) if ans1 else None)

    segments = build_segments(coords)
    ans2 = 0
    i = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            i += 1
            if i % 100 == 0:
                print(f"{i}/{len(coords)*len(coords)}")
            dx = abs(x2-x1) + 1
            dy = abs(y2-y1) + 1
            a = abs(dx) * abs(dy)
            if a < ans2:
                continue
            r = to_rect_inner(x1, y1, x2, y2)
            if not any(intersects(s, r) for s in segments):
                ans2 = a
    ctx.submit(2, str(ans2) if ans2 else None)
