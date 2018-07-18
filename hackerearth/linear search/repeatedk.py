n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
k=int(input())
count=[0]*(l[-1]+1)
for i in l:
    count[i]+=1
# print(count)
for i in range(len(count)):
    if(count[i]==k):
        print(i)
        break
