def appendAndDelete(s, t, k):
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1

    s1 = len(s[i:])
    t1 = len(t[i:])

    if s1 + t1 > k:
        return 'No'
    elif s1 + t1 == k:
        return 'Yes'
    elif len(s) + len(t) <= k:
        return 'Yes'
    elif abs(len(s) - len(t) - k) % 2 == 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)