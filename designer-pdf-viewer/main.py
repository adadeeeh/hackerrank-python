def designerPdfViewer(h, word):
    char = list("abcdefghijklmnopqrstuvwxyz")

    letters = list(word)

    height = []

    for letter in letters:
        i = char.index(letter)

        height.append(h[i])

    maxHeight = max(height)

    return maxHeight * len(letters)

if __name__ == "__main__":
    h = list(map(int, input().strip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)
    