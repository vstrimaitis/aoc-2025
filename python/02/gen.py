
from random import randint, shuffle
N = 50
MAX = 10**13
MAX_LEN = MAX // N
lo = 1
ranges = []
for i in range(N):
    length = randint(1, MAX_LEN)
    l = randint(lo, lo + MAX_LEN + 1 - length)
    r = l - 1 + length
    lo = r+1
    ranges.append(f"{l}-{r}")

shuffle(ranges)
print(",".join(ranges))

# python gen.py > s1.txt
