def birthdayCakeCandles(arr):
    maxVal = max(arr)
    maxCount = 0
    for candle in arr:
        if candle == maxVal:
            maxCount += 1
    return maxCount

if __name__ == "__main__":
    count = int(input().strip())
    candles = []
    
    # for _ in range(count):
    #     candles.append(input().strip())

    candles = list(map(int, input().strip().split()))

    result = birthdayCakeCandles(candles)

    print(result)