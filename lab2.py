pt=input("enter pt:")
key= int(input("Enter key: "))

max=int(len(pt)/key)
print(max)


i=0
ek=key+1
j=0
while j<key:
    r1=""
    print("ek:",ek)
    print("i:",i)
    print("max:", max)
    while i < max:
        r1 = "".join([r1, pt[i*ek]])
        i=i+1
    i=1
    max=max+1
    ek=ek-1
    print(r1)
    j=j+1

