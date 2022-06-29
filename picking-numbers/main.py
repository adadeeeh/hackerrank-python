def pickingNumbers(a):
    longest = 0

    number = {}

    a = sorted(a)

    for num in a:
        if num in number.keys():
            number[num] += 1
        else:
            number[num] = 1

    for k in number.keys():
        tmp = number[k]

        if tmp > longest:
                longest = tmp
                tmp = 0

        if k + 1 in number.keys():
            tmp = number[k] + number[k + 1]

            if tmp > longest:
                longest = tmp
                tmp = 0

    return longest

if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().strip().split()))

    result = pickingNumbers(arr)

    print(result)