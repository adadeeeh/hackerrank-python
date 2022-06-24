def pageCount(n, p):
    if p == n or (n % 2 != 0 and p == n - 1) or p == 1:
        return 0

    pagesFront = 0
    pagesBack = 0
    for i in range(2, n+1, 2):
        pagesFront += 1
        if p == i or p == i + 1:
            break
    
    if n % 2 == 0:
        n = n - 1
        pagesBack += 1

    for i in range(n, 2, -2):
        if p == i or p == i - 1:
            break
        pagesBack += 1

    if pagesFront < pagesBack:
        return pagesFront
    else:
        return pagesBack

if __name__ == "__main__":
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)