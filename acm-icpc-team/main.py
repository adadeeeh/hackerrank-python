from itertools import combinations


def acmTeam(topic):
    # for i in range(0, len(topic) - 1):
    #     for j in range(i, len(topic)):

    max = 0
    team = 0
    comb = combinations(topic, 2)

    for c in comb:
        count = 0
        subjects = int(c[0]) + int(c[1])

        for i in str(subjects):
            if i != '0':
                count += 1

            if count > max:
                max = count
                team = 1
            elif count == max:
                team += 1

    return [max, team]

if __name__ == "__main__":
    first_input = list(map(int, input().strip().split()))

    n = first_input[0]

    m = first_input[1]

    topic = []

    for _ in range(n):
        topic_item = input().strip()
        topic.append(topic_item)

    result = acmTeam(topic)

    print(result)