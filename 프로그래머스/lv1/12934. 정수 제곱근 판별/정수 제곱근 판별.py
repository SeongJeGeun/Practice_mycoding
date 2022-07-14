import math
def solution(n):
    a = math.sqrt(n)
    if n % a == 0:
        return math.pow(a+1, 2)
    else:
        return -1