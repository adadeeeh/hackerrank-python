def kangaroo(x1, v1, x2, v2):
    
    while True:
        if x1 == x2:
            return "YES"
        if x1 > x2 and v1 > v2:
            return "NO"
        elif x2 > x1 and v2 > v1:
            return "NO"
        elif x1 != x2 and v1 == v2:
            return "NO"

        x1 += v1
        x2 += v2

if __name__ == "__main__":
    n = list(map(int, input().strip().split()))

    x1 = n[0]

    v1 = n[1]

    x2 = n[2]

    v2 = n[3]

    result = kangaroo(x1, v1, x2, v2)

    print(result)