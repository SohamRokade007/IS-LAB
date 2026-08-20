pt=input("Enter plain text:")
inc=int(input("Enter key value:"))
CT=""
for i in range(len(pt)):
  char=pt[i]
  if char.isupper():
    newchar=chr((ord(char)+inc-65)%26+65)
  elif char.islower():
    newchar=chr((ord(char)+inc-97)%26+97)
  else:
    newchar=char
  CT= "".join([CT, newchar])
print("Cipher Text:", CT)



DT=""
i=0
for i in range(len(CT)):
  char=CT[i]
  if char.isupper():
    newchar=chr((ord(char)-inc-65)%26+65)
  elif char.islower():
    newchar=chr((ord(char)-inc-97)%26+97)
  else:
    newchar=char
  DT= "".join([DT, newchar])
print("Deciphered Text:", DT)