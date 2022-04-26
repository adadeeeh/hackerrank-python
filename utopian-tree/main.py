def utopianTree(n):
    height = 1
    spring = 1

    for i in range(n):
        if spring == 1:
            height = height * 2
            spring = 0
        elif spring == 0:
            height = height + 1
            spring = 1

    print(height)

if __name__ == "__main__":
    testCase = int(input().strip())

    for i in range(testCase):
        n = int(input().strip())

        utopianTree(n)