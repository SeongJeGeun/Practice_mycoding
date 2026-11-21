hour, minute = map(int, input().split())
duration = int(input())
print(*divmod((hour * 60 + minute + duration) % (24 * 60), 60))
