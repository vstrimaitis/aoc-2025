from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft

@ft.cache
def dfs(u: str, target: str) -> int:
    if u == target:
        return 1
    ans = 0
    for v in adj[u]:
        ans += dfs(v, target)
    return ans

with PuzzleContext(year=2025, day=11) as ctx:
    ans1, ans2 = None, None

    adj = defaultdict(list)
    for l in ctx.lines:
        if not l:
            continue
        ws = words(l)
        u = ws[0]
        for v in ws[1:]:
            adj[u].append(v)

    ans1 = dfs("you", "out")
    ctx.submit(1, str(ans1) if ans1 else None)

    seqs = [
        ["svr", "fft", "dac", "out"],
        ["svr", "dac", "fft", "out"]
    ]
    for seq in seqs:
        s = 1
        for a, b in zip(seq, seq[1:]):
            s *= dfs(a, b)
        if s != 0:
            ans2 = s
            break
    ctx.submit(2, str(ans2) if ans2 else None)
