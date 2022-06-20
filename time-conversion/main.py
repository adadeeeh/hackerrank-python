def timeConversion(s):
    time = s.split(":")
    ampm = time[-1]

    if ampm[2:4] == "PM" and int(time[0]) < 12:
        hour = int(time[0]) + 12
        time[0] = str(hour)

    elif ampm[2:4] == "AM" and time[0] == "12":
        time[0] = "00"


    ampm = ampm[0:2]
    time[-1] = ampm

    return ":".join(time)

if __name__ == "__main__":
    s = input()

    result = timeConversion(s)

    print(result)