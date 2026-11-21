def solution(n):
    pairs, extra = divmod(n, 2)
    return "수박" * pairs + "수" * extra
