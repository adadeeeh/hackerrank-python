def hurdleRace(k, height):
    maxHeight = max(height)
    
    potion = maxHeight - k

    if potion < 0:
        potion = 0

    return potion

if __name__ == "__main__":
    first_input = list(map(int, input().strip().split()))

    n = first_input[0]

    k = first_input[1]

    height = list(map(int, input().strip().split()))

    result = hurdleRace(k, height)

    print(result)