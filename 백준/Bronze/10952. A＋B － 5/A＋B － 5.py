while True:
    first, second = map(int, input().split())
    if first == second == 0:
        break
    print(first + second)
