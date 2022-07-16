def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"
    
    counter = 0

    if not any(letter.isdigit() for letter in password):
        counter += 1

    if not any(letter.islower() for letter in password):
        counter += 1

    if not any(letter.isupper() for letter in password):
        counter += 1

    if not any(letter in special_characters for letter in password):
        counter += 1
    
    if n + counter < 6:
        return 6 - n

    return counter

if __name__ == "__main__":
    n = int(input().strip())

    password = input().strip()

    result = minimumNumber(n, password)

    print(result)