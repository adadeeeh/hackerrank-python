def workbook(n, k, arr):
    special = 0
    page = 0

    for problem in arr:
        
        page += 1
        counter = 0

        for i in range(1, problem+1):
            counter += 1
            
            if counter == k and i != problem:
                if i == page:
                    special += 1
                
                page += 1
                counter = 0
                continue

            if i == page:
                special += 1

    return special

if __name__ == "__main__":
    first_line = list(map(int, input().strip().split()))

    n = first_line[0]

    k = first_line[1]

    arr = list(map(int, input().strip().split()))

    result = workbook(n, k, arr)

    print(result)
