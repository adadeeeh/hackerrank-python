def jumpingOnClouds(c):
    position = 0
    jump = 0
    finsih = False

    while finsih == False:
        nextOne = False
        if c[position + 1] == 0:
            if position + 1 == len(c) - 1:
                jump = jump + 1
                break
            if c[position + 2] == 0:
                position = position + 2
            else:
                position = position + 1
            jump = jump + 1
        else:
            nextOne = True
        
        if nextOne == True:
            if c[position + 2] == 0:
                position = position + 2
                jump = jump + 1

        if position == len(c) - 1:
            finsih = True
            
    return jump

if __name__ == "__main__":
    n = int(input().strip())

    c = list(map(int, input().strip().split()))

    result = jumpingOnClouds(c)

    print(result)