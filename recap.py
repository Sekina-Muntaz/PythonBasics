names=(["keren","Richard","Kui","sekina"],1,2)
# # names[2]
# print(names[0][2])
# names[0][2]="Carol"
# print(names)
# dict={"user":"eunice",
#       "age":28}
# print(dict["age"])
# dict["age"]=dict["age"]+1
# print(dict["age"])

days=24
event="Birthdays are on {}".format(days)
print(event)

def compare(num1,num2):
      # use an inbuilt max function
      # print(max(num1,num2,num3))

      if num1>num2:
            return (num1)
      elif num2>num1:
            return (num2)
      else :
            print("They are equal")


lg=compare(230,20)
print(lg+10)

def addThreeNumbers(num1,num2,num3):
      return num1+num2+num3
t=addThreeNumbers(num1=2,num2=3,num3=4)
print(t)



# compare(10,20,50)


