import pandas as pd

ciphertext = ""

pt = input("Enter Plain Text : ").lower()
key = input("Enter key : ").lower()

alphabet = "abcdefghiklmnopqrstuvwxyz"

# Remove J and duplicate letters from key
key = key.replace("j", "i")
key = "".join(dict.fromkeys(key))

# Create remaining alphabet
letters = key + "".join(ch for ch in alphabet if ch not in key)

# Create 5x5 Playfair matrix
matrix = []
matrix.append(list(letters[:5]))
matrix.append(list(letters[5:10]))
matrix.append(list(letters[10:15]))
matrix.append(list(letters[15:20]))
matrix.append(list(letters[20:]))

df = pd.DataFrame(matrix)

print("\nPlayfair Matrix:")
print(df)


if len(pt) % 2 != 0:
    pt = pt + "z"

pt = pt.replace("j", "i")

j = 0
i = 0
a = {}

while j < len(pt):

    if j == len(pt) - 1:
        a[i] = [pt[j], "x"]
        j += 1
        i += 1

    elif pt[j] == pt[j + 1]:
        a[i] = [pt[j], "x"]
        j += 1
        i += 1

    else:
        a[i] = [pt[j], pt[j + 1]]
        j += 2
        i += 1

print("\nPlain Text Pairs:")
print(a)


i = len(a)

while i > 0:

    b = []
    b.extend(a[i - 1])

    print("\nPair:", b)

    i -= 1

    for j in range(5):
        for k in range(5):

            if b[0] == df.iloc[j, k]:
                k1 = j
                k2 = k

            if b[1] == df.iloc[j, k]:
                m1 = j
                m2 = k

    print("Positions:", k1, k2, m1, m2)

    # Same row
    if k1 == m1:

        k2 = (k2 + 1) % 5
        m2 = (m2 + 1) % 5

    # Same column
    elif k2 == m2:

        k1 = (k1 + 1) % 5
        m1 = (m1 + 1) % 5

    # Rectangle
    else:

        k2, m2 = m2, k2

    c1 = df.iloc[k1, k2]
    c2 = df.iloc[m1, m2]

    ciphertext = c1 + c2 + ciphertext

    print("Encrypted pair:", c1 + c2)


print("\nCipher Text:", ciphertext)


decryptedtext = ""

# Ciphertext is already in correct order
i = 0

while i < len(ciphertext):

    b1 = ciphertext[i]
    b2 = ciphertext[i + 1]

    # Find positions of both characters
    for j in range(5):
        for k in range(5):

            if b1 == df.iloc[j, k]:
                k1 = j
                k2 = k

            if b2 == df.iloc[j, k]:
                m1 = j
                m2 = k

    print("\nCipher Pair:", b1 + b2)
    print("Positions:", k1, k2, m1, m2)

    # Same row
    if k1 == m1:

        k2 = (k2 - 1) % 5
        m2 = (m2 - 1) % 5

    # Same column
    elif k2 == m2:

        k1 = (k1 - 1) % 5
        m1 = (m1 - 1) % 5

    # Rectangle
    else:

        k2, m2 = m2, k2

    p1 = df.iloc[k1, k2]
    p2 = df.iloc[m1, m2]

    decryptedtext += p1 + p2

    print("Decrypted pair:", p1 + p2)

    i += 2


print("\nDecrypted Text:", decryptedtext)