#list manipulation

numbers=[1,2,3,4,5,6,7,8]

# popping-removes the last element of a list
print(numbers)
numbers.pop()
print(numbers)

# Append- adds elements to a list one at a time at the end of a list
empty=[2]
print(empty)
empty.append(1)
print(empty)

# replace number 3 with 11
numbers[2]=11
print(numbers)

name="Kivuti"

# print(name.replace())

# tuples
# immutable
days=("Mon","Tue","Wed","Thur","Fri","Sat","Sun")
print(days)
print(days[3])

# days[3]="march"
# print(days)


# Example
userName="Mark Zuckerberg"
password="pwd"

myDbValues=(1,"Mark Zuckerberg","password",38,"male",["value"])

myDbValues[5].append("key")
myDbValues[5].append({"mother":"teresa"})
print(myDbValues)


# myDbValues[0]=12
# print(myDbValues)

un=myDbValues[1]
print(un)

pss=myDbValues[2]
print(pss)

# ==strict equality operator
# = assignment operator
if un==userName:
    print("username true")
else:
    print("username false")

if pss==password:
    print("password true")
else:
    print("Wrong password")

# Dictionaries
# Stores data as Key Value pairs

myDictionary={"username":"mark zuckerberg","password":"pwd","age":38,"gender":"male"}
print(myDictionary["username"])
print(myDictionary["password"])
print(myDictionary["gender"])

self={
    "firstname":"Sekina",
    "lastname":"Muntaz",
    "Schools":{
        "primarySchools":[
            {
                "schoolName":"kilimani",
                "population":500,
                "headteacher":"Fridah"
            },{
                "schoolName":"milimani",
                "population":600,
                "headteacher":"Keren"
            },
        ]
    }
}
print(self["Schools"]["primarySchools"][1]["schoolName"])


# get users input from a console




