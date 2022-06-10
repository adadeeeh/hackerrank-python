def beautifulTriplets(d, arr):
    triplet = 0

    for i in arr:
        current = i
        temp = 1
        j = 0
        while j < 3:
        # while current <= max(arr):
            current = current + d
            if current in arr:
                temp += 1
                if temp == 3:
                    triplet += 1
                    break
            else:
                break

            j += 1
    
    return triplet

if __name__ == "__main__":
    first_input = list(map(int, input().strip().split()))

    n = first_input[0]

    d = first_input[1]

    arr = list(map(int, input().strip().split()))

    result = beautifulTriplets(d, arr)

    print(result)