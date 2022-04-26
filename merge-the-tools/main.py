def merge_the_tools(string, k):
    t = []
    n = len(string)
    for i in range(0, n, k ):
        t.append(string[i:i+k])

    for word in t:
        list_word = list(word)
        print(list_word, list(dict.fromkeys(list_word)))
        result = list(dict.fromkeys(list_word))
        print("".join(result))

if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)