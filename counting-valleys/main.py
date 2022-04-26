def countingValleys(steps, path):
    seaLevel = 0
    valley = 0

    for step in path:
        if step == "U":
            seaLevel += 1
            if seaLevel == 0:
                valley += 1
        elif step == "D":
            seaLevel -= 1
            
    print (valley)

if __name__ == "__main__":
    steps = int(input().strip())

    path = list(map(str, input().strip()))

    countingValleys(steps, path)