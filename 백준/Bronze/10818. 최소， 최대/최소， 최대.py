import sys

sys.stdin.buffer.readline()  # 첫 줄은 정수의 개수
numbers = map(int, sys.stdin.buffer.readline().split())
smallest = largest = next(numbers)
for value in numbers:
    if value < smallest:
        smallest = value
    elif value > largest:
        largest = value
print(smallest, largest)
