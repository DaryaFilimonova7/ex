n = int(input())

word = [str(x) for x in input()]

def s(word):
    i = 0
    while i < len(word):
        if i+1 < len(word):
            if word[i] > word[i + 1]:
                word = word[i + 1:]
                i = -1
        i += 1
    return(word)

ans = ''.join(s(word))
print(ans)
