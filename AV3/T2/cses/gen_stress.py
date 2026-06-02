import random
import sys

random.seed(42)
n = 20000
m = 200000
k = 10

lines = [f"{n} {m} {k}"]
for _ in range(m):
    a = random.randint(1, n)
    b = random.randint(1, n)
    while b == a:
        b = random.randint(1, n)
    c = random.randint(1, 100)
    lines.append(f"{a} {b} {c}")

sys.stdout.write('\n'.join(lines) + '\n')
