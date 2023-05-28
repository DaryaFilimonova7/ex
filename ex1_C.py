from collections import Counter

ans = [int(n1) for n1 in str(input())]
guess = [int(n2) for n2 in str(input())]

bull = 0
cow = 0
counts = Counter(ans)

for i,j in zip(ans, guess):
    if i==j:
        bull += 1
        if counts[i]:
            counts[i] -= 1
        else:
            cow -= 1
    elif counts[j]:
        cow += 1
        counts[j] -= 1

print(bull)
print(cow)
