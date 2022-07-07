def libraryFine(returnDate, dueDate):
    if returnDate == dueDate:
        return 0

    for i in range(2, -1, -1):
        if returnDate[i] != dueDate[i]:
            if returnDate[i] < dueDate[i] and i == 0:
                return 0

            if returnDate[i] < dueDate[i] and i == 1:
                return 0

            if returnDate[2] < dueDate[2] and i == 2:
                return 0

            if returnDate[i] > dueDate[i] and i == 0:
                return 15 * (returnDate[i] - dueDate[i])

            if returnDate[i] > dueDate[i] and i == 1:
                return 500 * (returnDate[i] - dueDate[i])

            if returnDate[i] > dueDate[i] and i == 2:
                return 10000

if __name__ == "__main__":
    returnDate = list(map(int, input().strip().split()))

    dueDate = list(map(int, input().strip().split()))

    result = libraryFine(returnDate, dueDate)

    print(result)
