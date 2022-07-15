def camelCase(s):
    word = 1

    for letter in s:
        if letter.isupper():
            word += 1

    return word

if __name__ == "__main__":
    s = input().strip()

    result = camelCase(s)

    print(result)