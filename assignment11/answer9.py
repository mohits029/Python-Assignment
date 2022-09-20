n= 2
b= 0
i= 0
lst1= []
str1= ""


while b<=n:
    b= 2**i
    lst1.append(b)
    i+= 1


for i in range(len(lst1)-1, -1, -1):
    if(lst1[i]<=n):
        n= n-lst1[i]
        str1= str1+ "1"
    else:
        str1= str1+ "0"



print(str1)