def findTotal(m,e,k,sci,sst):
    """find total marks"""
    return m+e+k+sci+sst
x=findTotal(m=60,e=70,k=50,sci=70,sst=68)

def findAverage(totalMarks):
    average=totalMarks/5
    return average
averageMarks=findAverage(x)


def findGrade(averageMarks):
    if averageMarks >= 80 and averageMarks <= 100:
        return "A"
    elif averageMarks >= 75 and averageMarks <= 79:
        return "A-"
    elif averageMarks >= 70 and averageMarks <= 74:
        return "B+"
    elif averageMarks >= 65 and averageMarks <= 69:
        return "B"
    elif averageMarks >= 60 and averageMarks <= 64:
        return "B-"
    elif averageMarks >= 55 and averageMarks <= 59:
        return "C+"
    elif averageMarks >= 50 and averageMarks <= 54:
        return "C"
    elif averageMarks >= 45 and averageMarks <= 49:
        return "C-"
    elif averageMarks >= 40 and averageMarks <= 44:
        return "D+"
    elif averageMarks >= 35 and averageMarks <= 39:
        return "D"
    elif averageMarks >= 30 and averageMarks <= 34:
        return "D-"
    elif averageMarks >= 0 and averageMarks <= 29:
        return "E"
    else:
        return "Check your average"

print(x)
print(averageMarks)
grade=findGrade(averageMarks)
print(grade)

