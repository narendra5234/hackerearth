for i in range(int(input())):
    l=input()
    if("21" in l or int(l)%21==0):
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")