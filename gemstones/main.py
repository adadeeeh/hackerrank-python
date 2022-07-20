from typing import Counter


def gemstones(n, arr):
    arr2 = []
    result = 0

    for rock in arr:
        rockCounter = Counter(rock)
        for k in rockCounter.keys():
            arr2.append(k)

    arr = "".join(arr2)
    c = Counter(arr)

    for k, v in c.items():
        if v == n:
            result += 1

    return result

if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().strip())

    result = gemstones(n, arr)

    print(result)