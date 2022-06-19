A,B = input().split()
C = input()
A = int(A)
B = int(B)
C = int(C)
hour = int((60 * A + B + C) / 60)
min = (60 * A + B + C) % 60
if hour >= 24:
    print(hour -24, min)
else:
    print(hour, min)