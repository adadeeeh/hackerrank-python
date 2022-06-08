def taumBday(b, w, bc, wc, z):
    if bc > wc + z:
        bc = wc + z
    elif wc > bc + z:
        wc = bc + z
    
    cost = b * bc + w * wc
    return cost

if __name__ == "__main__":
    t = int(input().strip())

    for i in range(t):
        first_line = list(map(int, input().strip().split()))

        b = first_line[0]

        w = first_line[1]

        second_line = list(map(int, input().strip().split()))

        bc = second_line[0]

        wc = second_line[1]

        z = second_line[2]

        result = taumBday(b, w, bc, wc, z)

        print(result)