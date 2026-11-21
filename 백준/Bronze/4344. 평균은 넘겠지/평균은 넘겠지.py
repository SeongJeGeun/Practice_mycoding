for _ in range(int(input())):
    count, *scores = map(int, input().split())
    average = sum(scores) / count
    above_average = sum(score > average for score in scores)
    print(f"{above_average * 100 / count:.3f}%")
