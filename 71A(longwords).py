words = []

i = 1
N = int(input())

while i <= N:
    words.append(input())
    i = i + 1


for word in words:
    num = len(word) - 2
    if num > 8:
        print(word[0] + str(num) + word[-1])
    if num <= 8:
        print(word)
