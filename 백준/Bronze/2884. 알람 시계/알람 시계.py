hour, minute = map(int, input().split())
print(*divmod((hour * 60 + minute - 45) % (24 * 60), 60))
