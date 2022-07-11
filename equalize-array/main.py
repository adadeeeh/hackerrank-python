from collections import Counter

def equalizeArray(arr):
    arr.sort()
    newArr = Counter(arr)

    mostKey = newArr.most_common(1)[0]
    key = mostKey[0]
    
    del newArr[key]

    return sum(newArr.values())

if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().strip().split()))

    result = equalizeArray(arr)

    print(result)