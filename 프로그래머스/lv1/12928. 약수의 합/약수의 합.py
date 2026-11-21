from math import isqrt


def solution(n):
    total = 0
    for divisor in range(1, isqrt(n) + 1):
        if n % divisor == 0:
            partner = n // divisor
            total += divisor
            if partner != divisor:
                total += partner
    return total
