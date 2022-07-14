# from itertools import product


# def stones(n, a, b):
#     setLastNumber = set()

#     perm = product([a, b], repeat=n-1)

#     for i in list(perm):
#         lastNumber = sum(list((i)))

#         setLastNumber.add(lastNumber)
    
#     listLastNumber = list(setLastNumber)

#     listLastNumber.sort()

#     return listLastNumber

def stones(n, a, b):
    result = set()

    if a > b:
        a,b = b,a

    for i in range(n):
        lastNumber = (n - i - 1) * a + i * b
        result.add(lastNumber)

    result = list(result)
    result.sort()

    return result

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(result)

# 2
# 3
# 1
# 2
# 4
# 10
# 100

# 5
# 58
# 69
# 24
# 83
# 86
# 81
# 73
# 25
# 25
# 12
# 73
# 82
# 5
# 3
# 23