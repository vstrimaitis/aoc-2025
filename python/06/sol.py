from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

def rotate_ccw(arr: list[list[str]]) -> list[list[str]]:
    n = len(arr)
    m = len(arr[0])
    res = [[""] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[m - j - 1][i] = arr[i][j]
    return res

with PuzzleContext(year=2025, day=6) as ctx:
    
    ops = [s for s in ctx.lines[-1].split() if s]
    nums = [
        ints(s)
        for s in ctx.lines[:-1]
    ]
    ans1 = 0
    for j, op in enumerate(ops):
        xs = [l[j] for l in nums]
        if op == "+":
            ans1 += sum(xs)
        else:
            ans1 += ft.reduce(lambda a, b: a * b, xs)

    ctx.submit(1, str(ans1) if ans1 else None)

    arr = rotate_ccw([[c for c in l] for l in ctx.lines])
    lines = ["".join(row).replace(" ", "") for row in arr]
    lines = [s for s in lines if s]
    
    ans2 = 0
    xs = []
    for l in lines:
        x = ints(l)[0]
        xs.append(x)
        if l[-1] in "+*":
            if l[-1] == "+":
                ans2 += sum(xs)
            else:
                ans2 += ft.reduce(lambda a, b: a * b, xs)
            xs = []
        
    ctx.submit(2, str(ans2) if ans2 else None)
