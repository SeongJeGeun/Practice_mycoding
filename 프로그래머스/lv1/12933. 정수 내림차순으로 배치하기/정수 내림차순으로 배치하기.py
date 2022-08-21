def solution(n):
    x = [a for a in str(n)]
    answer = sorted(x, reverse = True)
    return int("".join(answer))