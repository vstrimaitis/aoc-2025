from collections import *
from typing import *
from heapq import *
from dataclasses import dataclass
from puzzle import PuzzleContext
from utils import *
import itertools as itt
import functools as ft
import z3

INF = 10**100

@dataclass
class Machine:
    lights: list[int]
    buttons: list[list[int]]
    joltages: list[int]

def parse_line(line: str) -> Machine:
    parts = line.split(" ")
    lights = [1 if c == "#" else 0 for c in parts[0][1:-1]]
    buttons = [ints(s) for s in parts[1:-1]]
    joltages = ints(parts[-1])
    return Machine(lights, buttons, joltages)

def part1(machine: Machine) -> int:
    best = INF
    for mask in range(1 << len(machine.buttons)):
        state = [0] * len(machine.lights)
        for i in range(len(machine.buttons)):
            if (mask >> i) & 1:
                for j in machine.buttons[i]:
                    state[j] ^= 1
        if state == machine.lights:
            best = min(best, bin(mask).count("1"))
    return best

def part1_z3(machine: Machine) -> int:
    solver = z3.Optimize()

    xs = [0] * len(machine.lights)
    counts = [z3.Int(f"c{i}") for i in range(len(machine.buttons))]
    for button, cnt in zip(machine.buttons, counts):
        solver.add(cnt >= 0)
        for j in button:
            xs[j] += cnt
    for x, val in zip(xs, machine.lights):
        solver.add(x % 2 == val)
    goal = sum(counts)
    solver.minimize(goal)

    assert solver.check() == z3.sat
    m = solver.model()
    ans = m.evaluate(goal).as_long()
    return ans

def part2(machine: Machine) -> int:
    solver = z3.Optimize()

    xs = [0] * len(machine.lights)
    counts = [z3.Int(f"c{i}") for i in range(len(machine.buttons))]
    for button, cnt in zip(machine.buttons, counts):
        solver.add(cnt >= 0)
        for j in button:
            xs[j] += cnt
    for x, val in zip(xs, machine.joltages):
        solver.add(x == val)
    goal = sum(counts)
    solver.minimize(goal)

    assert solver.check() == z3.sat
    m = solver.model()
    ans = m.evaluate(goal).as_long()
    return ans

def solve(machines: list[Machine], single_solver: Callable[[Machine], int]) -> int:
    return sum(map(single_solver, machines))

with PuzzleContext(year=2025, day=10) as ctx:

    machines = list(map(parse_line, ctx.lines))
    
    ans1 = solve(machines, part1_z3)
    ctx.submit(1, str(ans1) if ans1 else None)

    ans2 = solve(machines, part2)
    ctx.submit(2, str(ans2) if ans2 else None)
