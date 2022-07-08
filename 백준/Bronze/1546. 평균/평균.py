n = int(input())
score = list(map(int,input().split())) #현재 score
m = max(score)
sum = 0
for k in range(n):
    score[k] = score[k] / m * 100
    sum += score[k]
print(sum/n)