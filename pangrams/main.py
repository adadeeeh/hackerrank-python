def pangrams(s):
    s = s.replace(" ", "").lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    pangrams = True

    for letter in alpha:
        if letter not in s:
            pangrams = False
    
    if pangrams == True:
        return "pangram"
    else:
        return "not pangram"

if __name__ == "__main__":
    s = input().strip()

    result = pangrams(s)

    print(result)

