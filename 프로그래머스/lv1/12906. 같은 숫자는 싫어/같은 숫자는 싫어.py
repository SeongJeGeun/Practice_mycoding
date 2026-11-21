def solution(arr):
    result = []
    for value in arr:
        if not result or value != result[-1]:
            result.append(value)
    return result
