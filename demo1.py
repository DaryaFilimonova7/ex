n = int(input())

word = input()

def generator(word: str, tail:str) -> str:
    if word == "":
        print(tail)
    for i in range(len(word)):
        generator(word[:i] + word[i+1:], tail + word[i])

print(generator(word, ""))
