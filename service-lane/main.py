def serviceLane(width, cases):
    result = []

    for case in cases:
        width2 = width[case[0]:case[1]+1]
        minWidth = min(width2)

        result.append(minWidth)

    return result

if __name__ == "__main__":
    first_input = list(map(int, input().strip().split()))

    n = first_input[0]

    t = first_input[1]

    width = list(map(int, input().strip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().strip().split())))

    result = serviceLane(width, cases)

    print(result)

# 8 5     
# 2 3 1 2 3 2 3 3
# 0 3
# 4 6
# 6 7
# 3 5
# 0 7