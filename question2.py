# find if the given number is a palindrome or not?
a=int(input("Enter a number:"))
c=0
while a!=0:
    b=a%10
    c=c*10+b
    a//=10
if a==c:
    print("It is a plaindrome")
else:
    print("It is not a palindrome")