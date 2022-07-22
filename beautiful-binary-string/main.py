def beautifulBinaryString(b):
    counter = 0
    b = b.replace("010", "b")

    for string in b:
        if string == "b":
            counter += 1
            
    return counter

if __name__ == "__main__":
    n = int(input().strip())

    b = input().strip()[0:n]

    result = beautifulBinaryString(b)

    print(result)