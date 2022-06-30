def saveThePrisoner(n, m, s):
    turn = m % n

    if turn == 0:
        turn = m

    position = (s - 1) + turn

    if position > n:
        mult = position // n

        position = position - mult * n

        if position == 0:
            position = n

    return position

if __name__ == "__main__":
    t = int(input().strip())

    for i in range(0, t):
        first_line = list(map(int, input().strip().split()))

        n = first_line[0]

        m = first_line[1]

        s = first_line[2]

        result = saveThePrisoner(n, m, s)

        print(result)