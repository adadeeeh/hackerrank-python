def funnyString(s):
    sReverse = s[::-1]

    ascii = []
    asciiReverse = []
    diff = []
    diffReverse = []

    for char in s:
        ascii.append(ord(char))

    for char in sReverse:
        asciiReverse.append(ord(char))

    for i in range(0, len(ascii) - 1):
        diff.append(abs(ascii[i] - ascii[i + 1]))

    for i in range(0, len(asciiReverse) - 1):
        diffReverse.append(abs(asciiReverse[i] - asciiReverse[i + 1]))

    if diff == diffReverse:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == "__main__":
    q = int(input().strip())

    for _ in range(q):
        s = input()

        result = funnyString(s)

        print(result)