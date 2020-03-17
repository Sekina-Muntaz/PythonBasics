word="Hello world"

# checks the length of a word
print(len(word))
# prints number of times a word appears
print(word.count("l"))
# find the letters World in the string
print(word.index("world"))

# String replace
print(word.replace("Hello", "Goodbye"))

# String concatenation
a="mangoes"
b="oranges"
print(a +" "+b)

# String Formating
# using fstring
name=input("Enter your name")
lname=input("enter your last name")
fruit=input("What is your favorite fruit")

print(f"My name is:{name}{lname}")
print(f"My favourite fruit is:{fruit}")


