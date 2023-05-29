n = int(input())
a = [int(x) for x in input().split()]

def solve(a):
    if not a:
        return 0
    l, r = 0, len(a) - 1
    max_l, max_r = a[l], a[r]
    water = 0
    while l < r:
        if max_l >= max_r:
            water += max_r - a[r]
            r -= 1

            max_r = max(max_r, a[r])
        
        else:
            water += max_l - a[l]
            l += 1

            max_l = max(max_l,a[l])

    return water


print(solve(a))
