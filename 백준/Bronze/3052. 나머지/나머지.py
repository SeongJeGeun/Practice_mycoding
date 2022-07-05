B = []
for i in range(10):
    A = int(input())
    B.append(A%42)
B = set(B)
print(len(B))