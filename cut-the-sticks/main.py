import time
from turtle import st

def cutTheSticks(sticks):
    sticksCut = []

    while True:
        print(len(sticks))
        sticksLength = []
        minValue = min(sticks)

        sticksCut.append(len(sticks))
        for stick in sticks:
            length = stick - minValue
            if length == 0:
                continue
            sticksLength.append(length)
        
        sticks = sticksLength

        if len(sticks) == 0:
            break
        
if __name__ == "__main__":
    n = int(input().strip())
    
    sticks = []

    # for _ in range(n):
    #     sticks.append(int(input().strip()))

    sticks = list(map(int, input().strip().split()))

    cutTheSticks(sticks)