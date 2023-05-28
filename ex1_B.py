n = int(input())
a = [int(n1) for n1 in input().split()]


def find_max() -> int:
    for i in a[1:len(a)]:
        max_m = max(a)
        if max_m == a[i] and i != 0 and i != len(a):
            return max_m
       


max_idx = find_max()
print(max_idx)
