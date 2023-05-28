ans = [int(n1) for n1 in str(input())]
guess = [int(n2) for n2 in str(input())]

bull = 0
cow = 0

for i in range(len(ans)):
        if guess[i] == ans[i]:
            bull += 1
        if ans[i] in guess:
            cow += 1
cow = cow - bull

print(bull)
print(cow)


# 9 тест не проходит
