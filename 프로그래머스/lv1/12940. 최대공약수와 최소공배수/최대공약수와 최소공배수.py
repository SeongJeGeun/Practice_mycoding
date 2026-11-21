from math import gcd


def solution(n, m):
    divisor = gcd(n, m)
    return [divisor, n // divisor * m]
