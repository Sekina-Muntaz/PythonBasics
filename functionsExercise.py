
def findGrade(*args):
    totalMarks=0
    for each in args:
        totalMarks=totalMarks+each
    print(totalMarks)

    averageMarks=totalMarks/5
    print(averageMarks)

    if averageMarks >= 80 and averageMarks <= 100:
        print("Your Grade is", ": A")
    elif averageMarks >= 75 and averageMarks <= 79:
        print("Your grade is ", "B")
    elif averageMarks >= 70 and averageMarks <= 74:
        print("Your grade is", ": B+")
    elif averageMarks >= 65 and averageMarks <= 69:
        print("Your grade is", ": B")
    elif averageMarks >= 60 and averageMarks <= 64:
        print("Your grade is", ": B-")
    elif averageMarks >= 55 and averageMarks <= 59:
        print("Your grade is", ": C+")
    elif averageMarks >= 50 and averageMarks <= 54:
        print("Your grade is", ": C")
    elif averageMarks >= 45 and averageMarks <= 49:
        print("Your grade is", ": C-")
    elif averageMarks >= 40 and averageMarks <= 44:
        print("Your grade is", ": D+")
    elif averageMarks >= 35 and averageMarks <= 39:
        print("Your grade is", ": D")
    elif averageMarks >= 30 and averageMarks <= 34:
        print("Your grade is", ": D-")
    elif averageMarks >= 0 and averageMarks <= 29:
        print("Your grade is", ": E")
    else:
        print("Check your marks again")

maths=int(input("Enter maths"))
english=int(input("Enter maths"))
kiswahili=int(input("Enter maths"))
science=int(input("Enter maths"))
sst=int(input("Enter maths"))


findGrade(50,50,50,50,50)



def sumDigits(*args):
    total=0
    for each in args:
        total=total+each
    print(total)

sumDigits(1,3,4,6,7)

