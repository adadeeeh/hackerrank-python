def miniMaxSum(arr):
    arr.sort()

    min = 0
    max = 0

    for i in range(len(arr)-1):
        min = min + arr[i]

    for i in range(1, len(arr)):
        max = max + arr[i]
        
    print (min, max)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))

    miniMaxSum(arr)