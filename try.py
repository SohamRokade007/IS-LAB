pt = input("Enter plaintext: ")
key = int(input("Enter key: "))

rails = [""] * key

row = 0
direction = 1

for ch in pt:
    rails[row] += ch

    if row == 0:
        direction = 1
    elif row == key - 1:
        direction = -1

    row += direction


for j in range(0,key):
    print(rails[j],end="")

print("")

