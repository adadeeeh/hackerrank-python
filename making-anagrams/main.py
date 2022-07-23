from typing import Counter


def makingAnagrams(s1, s2):
    finalWordCount = 0

    s1Sort = sorted(s1)
    s2Sort = sorted(s2)

    s1Count = Counter(s1Sort)
    s2Count = Counter(s2Sort)

    key = []

    # find the same char
    for k in s1Count.keys():
        if k in s2Count.keys():
            key.append(k)

    # count the final word
    for k in key:
        if abs(s1Count.get(k) - s2Count.get(k)) == 0:
            finalWordCount += s1Count.get(k)
        elif s1Count.get(k) < s2Count.get(k):
            finalWordCount += s1Count.get(k)
        else:
            finalWordCount += s2Count.get(k)
        
    deletionCount = (len(s1) - finalWordCount) + (len(s2) - finalWordCount)

    return deletionCount

if __name__ == "__main__":
    s1 = input().strip()

    s2 = input().strip()

    result = makingAnagrams(s1, s2)

    print(result)