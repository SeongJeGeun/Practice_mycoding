def solution(n):
    a = "수박" * n
    b = []
    for i in range(n):
        b.append(a[i])
    return "".join(b)