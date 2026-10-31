print("!!!=> WELCOME TO LAGBAJA SCHOOL RECORDS <=!!!")
print("_=_=> WHICH GRADE'S RECORD DO YOU WISH TO CREATE: <=_=_")
grade = int(input())

print("Number of students please: ")
numberOfStudents = int(input())
print("Saved--->")

print("Number of subjects taken please")
numberOfSubjects = int(input())
print("Saved--->")

print(f"_=_=> CREATING GRADE {grade} RECORDS SHEET <=_=_")
print("")

recordBook = [[0] * (numberOfSubjects + 3) for index in range(numberOfStudents)]
for index in range(numberOfStudents):
    i = index + 1
    print(f"NEW STUDENT: STUDENT {i}")
    print("")
    for index_a in range(numberOfSubjects):
        print("ENTER STUDENTS SUBJECT SCORE")
        score = int(input())
        while score < 0 or score > 100:
            print("invalid score")
            print("ENTER STUDENTS SUBJECT SCORE")
            score = int(input())
        recordBook[index][index_a] = score


for index in range(numberOfStudents):
    total = 0
    for index_a in range(numberOfSubjects):
        total += recordBook[index][index_a]
    recordBook[index][numberOfSubjects] = total

averages = [0.0] * numberOfStudents
for index in range(numberOfStudents):
    average = recordBook[index][numberOfSubjects] / numberOfSubjects
    averages[index] = average

for index in range(numberOfStudents):
    position = 1
    for index_a in range(numberOfStudents):
        if recordBook[index_a][numberOfSubjects] > recordBook[index][numberOfSubjects]:
            position += 1
    recordBook[index][numberOfSubjects + 2] = position


print("=======================================================================")
print(f"Class{grade}|", end="")

for index in range(1, numberOfSubjects + 1):
    print(f" \t subject{index} \t ", end="")
print(" \t TOT \t AVE \t POS")
print("=======================================================================")

for index in range(numberOfStudents):
    print(f"Student {index + 1} |", end="")
    for index_a in range(numberOfSubjects):
        print(f" \t {recordBook[index][index_a]} \t ", end="")
    print(f" \t {recordBook[index][numberOfSubjects]} \t {averages[index]:.2f} \t {recordBook[index][numberOfSubjects + 2]}")
print("=======================================================================")
print("=======================================================================")

print("SUBJECT SUMMARY")
passes = [0] * numberOfSubjects
fails = [0] * numberOfSubjects
overallHighest = recordBook[0][0]
overallHighestStudent = 0
overallHighestSubject = 0
overallLowest = recordBook[0][0]
overallLowestStudent = 0
overallLowestSubject = 0

for index_a in range(numberOfSubjects):
    highest = recordBook[0][index_a]
    highestStudent = 0
    lowest = recordBook[0][index_a]
    lowestStudent = 0
    subjectTotal = 0

    for index in range(numberOfStudents):
        mark = recordBook[index][index_a]
        subjectTotal += mark

        if mark > highest:
            highest = mark
            highestStudent = index
        if mark < lowest:
            lowest = mark
            lowestStudent = index
        if mark >= 50:
            passes[index_a] += 1
        else:
            fails[index_a] += 1

    if highest > overallHighest:
        overallHighest = highest
        overallHighestStudent = highestStudent
        overallHighestSubject = index_a
    if lowest < overallLowest:
        overallLowest = lowest
        overallLowestStudent = lowestStudent
        overallLowestSubject = index_a

    print(f"Subject {index_a + 1}")
    print(f"Highest scoring student is: Student {highestStudent + 1} scoring {highest}")
    print(f"Lowest scoring student is: Student {lowestStudent + 1} scoring {lowest}")
    print(f"Total score is: {subjectTotal}")
    print(f"Average score is: {subjectTotal / numberOfStudents:.2f}")
    print(f"Number of passes: {passes[index_a]}")
    print(f"Number of fails: {fails[index_a]}")
    print("")

hardest = 0
easiest = 0
for index_a in range(1, numberOfSubjects):
    if fails[index_a] > fails[hardest]:
        hardest = index_a
    if passes[index_a] > passes[easiest]:
        easiest = index_a
print(f"The hardest subject is Subject {hardest + 1} with {fails[hardest]} failures")
print(f"The easiest subject is Subject {easiest + 1} with {passes[easiest]} passes")
print(f"The overall highest score is scored by Student {overallHighestStudent + 1} in subject {overallHighestSubject + 1} scoring {overallHighest}")
print(f"The overall lowest score is scored by Student {overallLowestStudent + 1} in subject {overallLowestSubject + 1} scoring {overallLowest}")
print("=======================================================================")

bestStudent = 0
worstStudent = 0
classTotal = 0
for index in range(numberOfStudents):
    classTotal += recordBook[index][numberOfSubjects]
    if recordBook[index][numberOfSubjects] > recordBook[bestStudent][numberOfSubjects]:
        bestStudent = index
    if recordBook[index][numberOfSubjects] < recordBook[worstStudent][numberOfSubjects]:
        worstStudent = index

print("")
print("CLASS SUMMARY")
print("=======================================================================")
print(f"Best graduating student is: Student {bestStudent + 1} scoring {recordBook[bestStudent][numberOfSubjects]}")
print("=======================================================================")
print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(f"Worst graduating student is: Student {worstStudent + 1} scoring {recordBook[worstStudent][numberOfSubjects]}")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")
print("=======================================================================")
print(f"Class total score is: {classTotal}")
print(f"Class average score is: {classTotal / numberOfStudents:.1f}")
print("=======================================================================")
print("THANK YOU FOR USING OUR RECORD SYSTEM!\\(O-O)/")
