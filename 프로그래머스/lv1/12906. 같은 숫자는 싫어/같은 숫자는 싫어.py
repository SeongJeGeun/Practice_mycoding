def solution(arr):
    answer = []
    li1 = 0
    for i in arr:
        if i != li1:
            answer.append(i)
        else:
            pass
        li1 = i
    return answer