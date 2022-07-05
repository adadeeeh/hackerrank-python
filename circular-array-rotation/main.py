def circularArrayRotation(a, k, queries):
    arr = a.copy()
    answer = []

    for i in range(len(a)):
        index = i + k

        index = index % len(a)

        arr[index] = a[i]

    for q in queries:
        answer.append(arr[q])

    return answer

if __name__ == "__main__":
    first_line = list(map(int, input().strip().split()))

    n = first_line[0]

    k = first_line[1]

    q = first_line[2]

    a = list(map(int, input().strip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print(result)
