# List
taskList=[23,"Jane",["Lesson 23",560,{"currency":"KES"}],987,(76,"John")]

# Determing type of variable in taskList using an inbuilt function
print(type(taskList))

# Print KES
print(taskList[2][2]["currency"])

# Print 560
print(taskList[2][1])


# Use a function to determine the length of taksList
print(len(taskList))

# Change 987 to 789 without using an inbuilt -method (I.e Reverse
print(taskList)
taskList[3]=789
print(taskList)

# Change the name “John” to “Jane” .
print(taskList[4])
# A tuple is immutable

# 2
# Print max element in a list
ls1 = [123,34,54645,34,5]

print((max(ls1)))


# Given the dictionary below find the max profit

profit= {
                              "cost_price": 32.67,
                              "sell_price": 45.00,
                              "inventory": 1200
                            }
a=profit["cost_price"]
b=profit["sell_price"]
c=profit["inventory"]

maxProfit=a+b+c
print(maxProfit)

# Input from console
prompt=input("Type something")

# yourInput=prompt

print("Your input is",prompt)

