n = int(input())
s = []
l = list(map(int, input().split()))

sum = 0
for i in l:
    sum += i
    s.append(sum)
for i in range(int(input())):
    x = int(input())
    c = 0
    for i in range(len(s)):
        if (x <= s[i]):
            print(i + 1)
            break
        else:
            c += 1
    if (c == len(s)):
        print("-1")

