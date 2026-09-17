CT=(input("Enter Cipher Text: "))

for inc in range (1,26):
    DT=""
    i=0
    for i in range(len(CT)):
        print(i)
        char=CT[i]
        if char.isupper():
            newchar=chr((ord(char)-inc-65)%26+65)
        elif char.islower():
            newchar=chr((ord(char)-inc-97)%26+97)
        else:
            newchar=char
        DT= "".join([DT, newchar])
    print("Deciphered Text for key ",inc, " :", DT)
    