n,q=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
low=0
high=n-1
for i in range(q):
    low,high,c=0,n-1,0
    k=int(input())
    while(low<=high):
        mid=(low+high)//2
        if(k>l[mid]):
            low=mid+1
        elif(k<l[mid]):
            high=mid-1
        elif(k==l[mid]):
            print("YES")
            break
    else:
        c+=1
    if(c==1):
        print("NO")

