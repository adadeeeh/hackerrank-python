def alternatingCharacters(s):
    counter = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            counter += 1

    return counter

if __name__ == "__main__":
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()

        result = alternatingCharacters(s)

        print(result)