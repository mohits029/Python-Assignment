n= 90030;
sum= 0;

while n>0:
    x= n%10;
    sum= sum+x;
    n= n//10;

print(sum)
