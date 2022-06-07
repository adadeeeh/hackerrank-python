def jumpingOnClouds(c, k):
    position = 0
    energy = 100

    while True:
        position = position + k
        
        if position >= len(c):
            position = position % len(c)

        if c[position] == 1:
            energy -= 3
        else:
            energy -= 1

        if position == 0:
            break

    return energy

if __name__ == "__main__":
    nk = input().strip().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().strip().split()))

    result = jumpingOnClouds(c, k)

    print(result)