#GRADING SYSTEM APPLICATION.
maths=int(input("Enter marks for maths: "))
english=int(input("Enter marks for english: "))
science=int(input("Enter marks for science: "))
kiswahili=int(input("Enter marks for kiswahili: "))
sst=int(input("Enter marks for sst: "))

print(type(sst))


# Finding total marks
totalMarks=(maths+english+kiswahili+science+sst)
print("Your total marks is: ",totalMarks)


# Finding average marks
averageMarks=(totalMarks/5)
print("Your average is: ",averageMarks)

# USING AVERAGE SCORE, GRADE THE STUDENT USING THE FOLLOWING GRADING SYSTEM

if averageMarks>=80 and averageMarks<=100:
    print("Your Grade is",": A")
elif averageMarks>=75 and averageMarks<=79:
    print("Your grade is ","B")
elif averageMarks >= 70 and averageMarks <= 74:
    print("Your grade is", ": B+")
elif averageMarks >= 65 and averageMarks <= 69:
    print("Your grade is", ": B")
elif averageMarks >=60 and averageMarks <= 64:
    print("Your grade is", ": B-")
elif averageMarks >= 55 and averageMarks <= 59:
    print("Your grade is", ": C+")
elif averageMarks >=50 and averageMarks<=54:
    print("Your grade is",": C")
elif averageMarks>=45 and averageMarks<=49:
    print("Your grade is",": C-")
elif averageMarks>=40 and averageMarks<=44:
    print("Your grade is",": D+")
elif averageMarks>=35 and averageMarks<=39:
    print("Your grade is",": D")
elif averageMarks>=30 and averageMarks<=34:
    print("Your grade is",": D-")
elif averageMarks>=0 and averageMarks<=29:
    print("Your grade is",": E")
else:
    print("Check your marks again")
