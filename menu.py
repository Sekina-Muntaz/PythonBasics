print("1. 20MB")
print("2. 30MB")
print("3. 40MB")

choice=int(input("enter selection: "))
print(type(choice))

if choice==1:
    print("You have bought 20MB")
elif choice==2:
    print("You have bought 30MB")
elif choice==3:
    print("You have bought 40MB")
else:
    print("invalid")


