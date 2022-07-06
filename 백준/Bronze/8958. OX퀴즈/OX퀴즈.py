n = int(input())
for _ in range(n):
    a = list(input())
    score = 0
    sum = 0
    for h in a:
        if h == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)