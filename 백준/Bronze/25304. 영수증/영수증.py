buy_p = int(input())
buy_c = int(input())
sum = 0
for i in range(buy_c):
    a = list(map(int, input().split()))
    sum += a[0] * a[1]
if buy_p - sum == 0:
    print('Yes')
else:
    print('No')