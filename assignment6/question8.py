# d= b**2 -4ac

print("Enter coffiecient of x squre, Enter Coffiecient of x and the constent term: ")
a,b,c= int(input()), int(input()), int(input())

d= (b**2)-(4*a*c)
if d>0:
    print("Real and Distinct roots")
elif d==0:
    print("Real and Equal roots")
else:
    print("Imaginary roots")