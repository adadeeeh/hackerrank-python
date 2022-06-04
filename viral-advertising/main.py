def viralAdvertising(n):
    totalLikes = 0
    shared = 5
    for i in range(1, n+1):
        liked = shared // 2
        totalLikes = totalLikes + liked

        shared = liked * 3
    
    return totalLikes

if __name__ == "__main__":
    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)