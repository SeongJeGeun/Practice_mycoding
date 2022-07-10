c = int(input())
for i in range(c):
    count = 0
    score = list(map(int, input().split()))
    average1 = sum(score[1:]) / score[0]
    percent  = 100 / score[0]
    for j in score[1:]:
        if average1 < j:
            count +=1
    a = percent * count
    print(f'{a:.3f}%')