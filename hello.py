pt=input("Enter plain text:")
inc=int(input("Enter key value:"))
lenght=len(pt)
print(lenght)
i=0
CT=""
for text in pt:
  asc=ord(pt[i])
  newasc=asc+inc
  newchar=chr(newasc)
  print(newchar)
  CT= "".join([CT, newchar])
  i=i+1


print("Cypher Text:",CT)

j=0
dec=""
for text in pt:
  asc=ord(CT[j])
  newasc=asc-inc
  newchar=chr(newasc)
  print(newchar)
  dec= "".join([dec, newchar])
  j=j+1


print("Decrepted text:",dec)
