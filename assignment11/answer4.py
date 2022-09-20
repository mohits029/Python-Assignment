num= int(input("Enter n Value: "))
x=0
for i in range(1,num+1):
    if(i%2!=0):
        sq= i*i
        x= x+sq

print("Sum of squre of n odd natural number is: ",x)