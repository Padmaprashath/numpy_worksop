#write a program to find the sum of digits of a given number'
a=int(input("Enter a digit:"))
c=0
while a!=0:
    b=a%10
    c=c+b
    a//=10
print("The sum of the given digits:",c)