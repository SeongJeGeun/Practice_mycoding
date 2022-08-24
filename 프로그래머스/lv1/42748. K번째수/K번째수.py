def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        d = array[i-1:j]
        d.sort()
        t = d[k-1]
        answer.append(t)
    return answer
