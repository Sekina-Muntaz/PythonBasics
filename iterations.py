
classAttendance=["Buom", "keren","Eunice","Richard","Kui","Sekina"]

# add Fridah

classAttendance.append("Fridah")
classAttendance.append("Caleb")

#
# print(classAttendance[0])
# print(classAttendance[1])
# print(classAttendance[2])
# print(classAttendance[3])
# print(classAttendance[4])
# print(classAttendance[5])
# print(classAttendance[6])

# for loop
for each in classAttendance:
    print(each)
# iterating over a string
letters="abcdefghijk"
for letter in letters:
    print(letter)
# iterating over a tuple
numbers=(1,2,3,4,5,6)
for number  in numbers:
    print(number)

# using for and if
line=list(range(1,101))
print(type(line))
print(line)

for each in line:
    if each%2==0:
        print("yaay")
    else:
        print("naay")

