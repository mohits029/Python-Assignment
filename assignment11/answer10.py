n= 57
x= 0
while n!=0:
    x= (x*10) + (n%8)
    n= n//8

oct= 0
while x!=0:
    oct= (oct*10) + (x%10)
    x= x//10
print(oct)

