def migratoryBirds(arr):
    birdCount = [0, 0, 0, 0, 0, 0]

    for bird in arr:
        birdCount[bird] += 1

    return birdCount.index(max(birdCount))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().strip().split()))

    result = migratoryBirds(arr)

    print(result)