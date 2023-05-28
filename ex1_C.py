ans = [int(n1) for n1 in str(input())]
guess = [int(n2) for n2 in str(input())]

bull_cow = [0, 0]
for i, j in zip(ans, guess):
    if j in ans:
        if j == i:
            bull_cow[0] += 1
        else:
            if j not in guess[:j]:
                bull_cow[1] += 1
print(bull_cow[0])
print(bull_cow[1])

# 5 тест не проходит
