def permutationEquation(arr):
    result = []

    for i in range(1, n+1):
        index = arr.index(i)
        index = index + 1

        y = arr.index(index)
        y += 1
        
        result.append(y)
        print(y)
    
    return result

if __name__ == "__main__":
    n = int(input().strip())

    p = list(map(int, input().strip().split()))

    result = permutationEquation(p)