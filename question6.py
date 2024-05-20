#write a program to find the maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
maximum = max_of_two(num1, num2)
print(f"The maximum of {num1} and {num2} is {maximum}.")
