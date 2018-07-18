l="SUVO"
m="SUVOJIT"
for i in range(int(input())):
    s=input()
    c, d = 0, 0
    for j in range(len(s)-6):
        if(s[j:j+7]==m):
            c+=1
            break
    # print(c)
    if(c!=0):
        new = s[:j] + s[j + 7:]
    else:
        new=s
    for j in range(len(new) - 3):
        if (new[j:j + 4] == l):
            d+=1
            break

    print('SUVO = %i, SUVOJIT = %i'%(d,c))



