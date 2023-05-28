a = input()

num = [int(i) for i in str(a)]


def rec_sum(x) -> int:
    a_sum = sum(x)
    if a_sum < 10:
        return a_sum
    while a_sum >= 10:
        x = [int(i) for i in str(a_sum)]
        return rec_sum(x)


ans = rec_sum(num)
print(ans)
