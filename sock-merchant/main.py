def sockMerchant(socks):
    pair = 0
    try:
        for i in range(len(socks)):
            remove = socks.pop(0)
            try:
                socks.remove(remove)
                print(socks)
                pair += 1
            except:
                None
    except:
        None

    return pair

if __name__ == "__main__":
    n = int(input().strip())

    socks = list(map(int, input().strip().split()))

    result = sockMerchant(socks)

    print(result)