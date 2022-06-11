def howManyGames(p, d, m, s):
    additional = 0

    while s >= 0:
        s = s - p

        if s < 0:
            break
        
        additional += 1
        p = p - d
        if p <= m:
            p = m

    return additional

if __name__ == "__main__":
    first_line = list(map(int, input().strip().split()))

    p = first_line[0]

    d = first_line[1]

    m = first_line[2]

    s = first_line[3]

    answer = howManyGames(p, d, m, s)

    print(answer)