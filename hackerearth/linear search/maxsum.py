n=int(input())
l=list(map(int,input().split()))
sum=0
c,d=0,0
for i in l:
    if(i<=0):
        d+=1
    if(i>=0):
        sum+=i
        c+=1
if(d==n):
    print(max(l),1)
else:
    print(sum,c)
