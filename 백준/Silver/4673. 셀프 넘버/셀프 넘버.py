limit = 10_000
generated = {number + sum(map(int, str(number))) for number in range(1, limit + 1)}
for number in range(1, limit + 1):
    if number not in generated:
        print(number)
