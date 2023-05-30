# Превышение ограничения по времени (я - 1,09, нужно - 1)

# Определить анаграмма или нет

a = input()
w1 = [str(x) for x in a]
b = input()
w2 = [str(x) for x in b]

w_1 = [str(x) for x in w1]
ans = ""
st = [0 for x in w2]


for i in range(len(w2)):
    for j in range(len(w_1)):
        if w_1[j] != "0":
            if w2[i] == w_1[j]:
                if st[i] == 0:
                    st[i] = 1
                    w_1[j] = '0'
                    break
                else:
                    ans = "NO"


if sum(st) == len(w2):
    ans = "YES"
else:
    ans = "NO"

print(ans)
