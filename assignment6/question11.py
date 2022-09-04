x= int(input("Enter Month Number: "))
if (x in (1,3,5,7,8,10,12)):
    print("31 Days")
elif(x in (4,6,9,11)):
    print("30 Days")
elif(x==2):
    print("28 or 29 Days")
else:
    print("You entered invalid value")
