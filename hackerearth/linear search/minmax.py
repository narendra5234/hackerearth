n=int(input())
l=list(map(int,input().split()))
s=sum(l)
l1=[]
for i in range(n):
    l1.append(s-l[i])
print(min(l1),max(l1))
# n=int(input())
# l=list(map(int,input().split()))
# s=[]
# for i in range(n):
#     s.append(sum(l[:i]+l[i+1:]))
# print(min(s))
# print(max(s))