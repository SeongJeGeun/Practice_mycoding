def solution(array, commands):
    answer = []
    for start, end, k in commands:
        section = sorted(array[start - 1:end])
        answer.append(section[k - 1])
    return answer
