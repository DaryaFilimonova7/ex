n = int(input())
n_bin = bin(n)[2:]

count = 0

digits = [int(i) for i in str(n_bin)]
while len(digits) > 0:
    if digits[len(digits) - 1] == 0:
        digits.pop(len(digits) - 1)
        count += 1
    else:
        digits[len(digits) - 1] = digits[len(digits) - 1] - 1
        count += 1

count -= 1
print(count)
