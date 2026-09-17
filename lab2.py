pt=input("enter pt:")
key= int(input("Enter key: "))

max=int(len(pt)/key)
print("len=",max)


i=0
ek=key+1
j=0
while j<key:
    r1=""
    print("ek:",ek)
    print("i:",i)
    print("max:", max)
    my_variables = [""] * key
    while i < max:
        print(pt[i*ek])
        my_variables[i] = "".join([my_variables[i], pt[i*ek]])
        i=i+1
    max=max+1
    ek=ek-1
    j=j+1
for k in range(0,len(pt)):
    print(my_variables[i])