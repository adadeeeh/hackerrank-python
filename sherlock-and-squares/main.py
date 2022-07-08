import math

def squares(a, b):
    counter = 0

    a1 = int(math.sqrt(a))
    b1 = int(math.sqrt(b))

    if a1 * a1 >= a:
        counter += 1

    counter = (b1 - a1) + counter
        
    return counter

if __name__ == "__main__":
    testCase = int(input().strip())

    for _ in range(testCase):
        case = list(map(int, input().strip().split()))

        a = case[0]

        b = case[1]

        result = squares(a, b)

        print(result)