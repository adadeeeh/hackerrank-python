def getTotalX(arr, brr):
    considered = []

    for i in range(max(arr), min(brr) + 1):
        for a in arr:
            if i % a == 0 and i not in considered:
                considered.append(i)
            elif i % a != 0:
                if i in considered:
                    considered.remove(i)
                break

        for b in brr:
            if b % i != 0 and i in considered:
                considered.remove(i)

    return len(considered)

if __name__ == "__main__":
    first_line = list(map(int, input().strip().split()))

    n = int(first_line[0])

    m = int(first_line[1])

    arr = list(map(int, input().strip().split()))

    brr = list(map(int, input().strip().split()))

    total = getTotalX(arr, brr)

    print(total)