
# TASK 1:
# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No".
# Hint: Use input () to get the persons input
string=input("Enter yes or no")

if string=="yes" or string=="Yes":
    print("yes")
else:
    print("no")


# TASK 2:
# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max () function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.

num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
# x=[num1,num2,num3]
# print(x)


def findGreatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return f"The greatest number is{num1}"
    elif num2>num1 and num2>num3:
        return f"The greatest number is{num2}"
    elif num3>num1 and num3>num2:
        return f"The greatest number is{num3}"
    # else:
    #     return "They are equal"
greatest=findGreatest(num1,num2,num3)
print(greatest)

# TASK 3:
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function
a=[5,10,15,20]

def fistAndLastElement(a):


    result=(a[0],a[-1])

    return result
newList=fistAndLastElement(a)
print(newList)

# TASK 4:
# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

number=int(input("enter a number"))

def oddEven(number):
    if number%2==0:
        return "Even number"
    else:
        return "Odd Number"
x=oddEven(number)
print(x)


# TASK 5:
# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line.

a=(1,2,3,4,5,6,7,8,9,10)
one=a[0:5]
two=a[5:10]

firsthalf=str(one).strip("()")
secondHalf=str(two).strip("()")


print(firsthalf)
print(secondHalf)


# Practice questions : PART C
# a) Create a function that takes a name and returns a greeting.
name=input("enter your name")
def greeting(name):
    # yourname=name// unneccesary
    return f"Hello,{name}"
result=greeting(name)
print(result)
# b) Write a function that takes the base and height of a triangle and return its area.
base=int(input("Enter the base"))
heights=int(input("Enter the height"))
def getArea(base,height):
    area=0.5*base*height

    return area
x=getArea(base,heights)
print("The area is:",x)

# c) Create a function that finds the maximum range of a triangles third edge
def maximumRange(side1,side2):
    maximumrange = (side1 + side2) - 1.

    return maximumrange
range=maximumRange(8,10)
print(range)

# d)Create a function that takes a list and returns the first element.
aList=[80,5,100]
def getFirstvalue(aList):
    return aList[0]
first=getFirstvalue(aList)
print(first)

# e)You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
#  Return the total number of legs on your farm
def numOfLegs(chicken,cows,pigs):
    chickenLegs=chicken*2
    cowLegs=cows*4
    pigLegs=pigs*4

    totalLegs=chickenLegs+cowLegs+pigLegs

    return totalLegs
allLegs=numOfLegs(5,2,8)
print(allLegs)

# f)Create a function that takes a list of numbers.
# Return the largest number in the list.
myList=[1000,1001,857,1]
def greatest(myList):
    return max(myList)
largest=greatest(myList)
print(largest)

# g)Given a list of integers,
# return the difference between the largest and smallest integers in the list.
numList=[10,15,20,2,10,6]
def difference(numList):
    largest=max(numList)
    smallest=min(numList)
    answer = largest - smallest

    return answer
diff=difference(numList)
print(diff)

# h. Create a function to concatenate two integer lists
def concat(list1,list2):
    return list1+list2

bigList=concat([1,2,3],[4,5,6])
print(bigList)

# i)Create a function that takes two strings as arguments and return either True or False
# depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
def comp(string1,string2):
    if len(string1)==len(string2):
        return True
    else:return False
checkedString=comp('ABC','CDE')
print(checkedString)

# j)Write a function that converts a dictionary into a list,
# where each element represents a key-value pair.
def dictToList(dictionary):
    temp=[]
    dictList=[]

    for key,value in dictionary.items():
        temp=[key,value]
        dictList.append(temp)
    return dictList

newList=dictToList({"name":"Sekina","age":"34"})
print(newList)

# k)You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
#  Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.
def profit(inventoryDict):
    inventory=inventoryDict["inventory"]
    costPrice=inventoryDict["cost_price"]
    sellPrice=inventoryDict["sell_price"]

    bp=inventory*costPrice
    sp=inventory*sellPrice

    actualProfit=sp-bp

    return actualProfit


actualProfit=profit({"cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200})
print(actualProfit)




















