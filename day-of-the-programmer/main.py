def dayOfProgrammer(year):
    if year == 1918:
        return "26.09." + str(year)
    else:
        if leap(year) == True:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)

def leap(year):
    if year > 1918:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)