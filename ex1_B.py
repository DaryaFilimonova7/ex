n = int(input())
a = [int(n1) for n1 in input().split()]


def find_max() -> int:
    for i in a[1:len(a)]:
        max_m = max(a)
        if max_m == a[i] and i != 0 and i != len(a):
            return i+1
       


max_idx = find_max()
print(max_idx)





# runtime error оба варианта






n = int(input())
a = [int(n1) for n1 in input().split()]


def find_max() -> int:
    found = False
    while not found:
        for i in a[1:len(a)]:
            max_m = max(a[1:len(a)-1])
            if max_m == a[i] and i != 0 and i != len(a)-1:
                found = True
                return i+1
            elif max_m == a[i] and (i == 0 or i == len(a)-1):
                a.pop(i)


max_idx = find_max()
print(max_idx)
