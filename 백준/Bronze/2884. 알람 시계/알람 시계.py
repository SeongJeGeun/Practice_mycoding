H, M = input().split()
H = int(H)
M = int(M)
if 0 < H and H <= 23 and M < 45:
    print(H-1,60-(45-M))
elif 45 <= M:
    print(H,M-45)
elif H ==0 and M < 45:
    print(23, 60-(45-M))