def countApplesAndOranges(s, t, a, b, apples, oranges):
    output = 0

    for apple in apples:
        if a + apple >= s and a + apple <= t:
            output += 1
    print(output)

    output = 0

    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            output += 1
    print(output)

if __name__ == "__main__":
    first_input = input().strip().split()

    s = int(first_input[0])

    t = int(first_input[1])

    second_input = input().strip().split()

    a = int(second_input[0])

    b = int(second_input[1])

    third_input = input().strip().split()

    m = int(third_input[0])

    n = int(third_input[1])

    apples = list(map(int, input().strip().split()))

    oranges = list(map(int, input().strip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)