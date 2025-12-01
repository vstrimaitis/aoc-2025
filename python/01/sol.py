from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft


with PuzzleContext(year=2025, day=1) as ctx:
    ans1, ans2 = 0, 0
    diffs = [int(l) for l in ctx.data.replace("R", "").replace("L", "-").split()]

    curr = 50
    for x in diffs:
        s = -1 if x < 0 else 1
        for _ in range(abs(x)):
            curr = (curr + s) % 100
            if curr == 0:
                ans2 += 1
        if curr == 0:
            ans1 += 1

    ctx.submit(1, str(ans1) if ans1 else None)
    ctx.submit(2, str(ans2) if ans2 else None)
