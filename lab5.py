import pandas as pd

choice = 0

while choice < 4:

    print("\n======= CRYPTOGRAPHY MENU ========")
    print("1. Caesar Cipher")
    print("2. Rail Fence Cipher")
    print("3. Playfair Cipher")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print("\n--- Caesar Cipher ---")

        text = input("Enter text: ")
        key = int(input("Enter key: "))

        result = ""

        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result += chr((ord(ch) - base + key) % 26 + base)
            else:
                result += ch

        print("Encrypted Text:", result)

    elif choice == 2:
        print("\n--- Rail Fence Cipher ---")
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



    elif choice == 3:

        print("\n--- Playfair Cipher ---")

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

    elif choice == 4:

        print("\nExiting Cryptography Menu...")
        break

    else:

        print("\nInvalid choice! Please enter 1-4.")
