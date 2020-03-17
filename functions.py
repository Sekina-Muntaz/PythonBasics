
# function: a block of code that performs a specific task
# parameters and arguments
# calling a function


# def is a keyword used for function declaration
# steps in function declaration
# functions can take more than one parameter
# 1.def
# 2. name of function
# 3.number and letter in this case is a parameter
# A parameter is a variable that tells a function the number of values to expect as input

def evenOdd(number):
    if number%2==0:
        print("even")
    else:
        print("odd")


# calling a function
# 5 and what are arguments
# An argument inputs to a function
evenOdd(5)

# function with more than one parameter
# def sum(a,b,c,d):
#     total=a+b+c+d
#     print(total)
#
# sum(1,2,3,4)


def test():
    name=input("Enter your name")
    print(f"My name is {name}")

test()
test()
test()





# positional and keyword arguments
# Args* and **kwargs
def addition(*args):
    # logic for getting sum goes here
   # print(sum(args))
    total=0
    for each in args:
        total=total+each
    print(total)




addition(10,40,80,10)
addition(30,40,50,60)
addition(70,80,90,99,100,200,34)

