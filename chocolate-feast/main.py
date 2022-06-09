def chocolateFeast(n, c, m):
    wrapper = n // c
    total = wrapper
    while wrapper // m > 0:
        wrapperLeft = wrapper % m
        wrapper = wrapper // m

        total = total + wrapper
        
        wrapper = wrapper + wrapperLeft
    
    return total

if __name__ == "__main__":
    t = int(input().strip())

    for i in range(t):
        first_line = list(map(int, input().strip().split()))

        n = first_line[0]

        c = first_line[1]

        m = first_line[2]

        result = chocolateFeast(n, c, m)

        print(result)