def fairRations(B):
    if sum(B) % 2 == 1:
        return "NO"

    bread = 0

    for i in range(0, len(B) - 1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i + 1] += 1
            bread += 2

        # first array is odd then add bread
    #     if i == 0:
    #         if B[i] % 2 == 1:
    #             B[i] += 1
    #             B[i + 1] += 1
    #             bread += 1

    #     # last array is odd then add bread
    #     elif i == len(B) - 1:
    #         if B[i] % 2 == 1:
    #             B[i] += 1
    #             B[i - 1] += 1
    #             bread += 1

    #     # check array except first and last
    #     else:
    #         if B[i] % 2 == 1:
    #             B[i] += 1
    #             bread += 1

    #             if B[i - 1] % 2 == 1:
    #                 B[i - 1] += 1
    #                 bread += 1
                
    #             elif B[i + 1] % 2 == 1:
    #                 B[i + 1] += 1
    #                 bread += 1

    #             else:
    #                 B[i + 1] += 1
    #                 bread += 1
        
    # for b in B:
    #     if b % 2 != 0:
    #         return "NO"

    return str(bread)

if __name__ == "__main__":
    n = int(input().strip())

    b = list(map(int, input().strip().split()))

    result = fairRations(b)

    print(result)
