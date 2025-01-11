#First of all, take two numbers from the user, store them in variables x and y, 
# respectively. Write a Python program to swap the values present inside x and y 
#  display the results

x=int(input("Enter the first number"))
y=int(input("Enter the second number"))

print("The value of x before swapping is ",x)
print("The value of y before swapping is ",y)

temp=x
x=y
y=temp

print("The value of x after swapping is ",x)
print("The value of y after swapping is ",y)