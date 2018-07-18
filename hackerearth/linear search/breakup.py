
N = int(input())
l = [0] * 30
for i in range(N):
    S = input().split(' ')
    if S[0] == 'G:':
        for j in S:
            if j.isdigit():
                l[int(j)-1] += 2
    elif S[0] == 'M:':
        for j in S:
            if j.isdigit():
                l[int(j)-1] += 1
for i in range(len(l)):
    if (max(l) == l[18] or max(l) == l[19]) and l[18]!=l[19]:
        print ("Date")
        break
    elif l.count(l[i]) != 1 and l[i] != 0:
        print ("No Date")
        break
    elif l[18] == l[19]:
        print ("No Date")
        break


