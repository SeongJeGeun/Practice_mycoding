import sys

lines = sys.stdin.buffer
count = int(next(lines))
for _ in range(count):
    first, second = map(int, next(lines).split())
    sys.stdout.write(f"{first + second}\n")
