a = input().split()
b = [1,1,2,2,2,8]
c = []
for i in a:
    c.append(int(i))
for i in range(len(b)):
    print(b[i] - c[i], end = ' ')