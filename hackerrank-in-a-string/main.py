def hackerrankInString(s):
    sCompare = "hackerrank"
    cursor = 0

    for char in s:
        if sCompare[cursor] == char:
            cursor += 1

        if cursor == 9:
            break
    
    if cursor == 9:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()

        result = hackerrankInString(s)

        print(result)