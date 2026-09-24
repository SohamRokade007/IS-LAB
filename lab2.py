pt = input("Enter PT: ")
key = int(input("Enter key: "))

max = int(len(pt) / key)
print("len =", max)

my_variables = [""] * key

i = 0
j = 0
direction = 1

while i < len(pt):

    my_variables[j] = my_variables[j] + pt[i]

    print("i:", i)
    print("j:", j)
    print("char:", pt[i])

    if j == 0:
        direction = 1
    elif j == key - 1:
        direction = -1

    j = j + direction
    i = i + 1

print("Rails:")

for k in range(key):
    print(my_variables[k])

ciphertext = ""

for k in range(key):
    ciphertext = ciphertext + my_variables[k]

print("Cipher Text:", ciphertext)