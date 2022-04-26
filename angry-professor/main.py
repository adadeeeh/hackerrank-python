def angryProfessor(treshold, students):
    count = 0
    for student in students:
        if student <= 0:
            count += 1
    
    if count >= treshold:
        print ("NO")
    else:
        print ("YES")

if __name__ == "__main__":
    testCase = int(input().strip())

    for i in range(testCase):
        case = input().strip().split()

        n = int(case[0])
        students = []

        treshold = int(case[1])


        students = list(map(int, input().strip().split()))
        # for _ in range(n):
        #     students.append(input().strip())
        
        angryProfessor(treshold, students)

