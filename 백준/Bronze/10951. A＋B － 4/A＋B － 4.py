import sys

for line in sys.stdin:
    first, second = map(int, line.split())
    print(first + second)
