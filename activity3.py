#Store the values of your first name and last name in respective variables.
#  Now add these two strings and store them in the variable full name.
#  Create another variable with the first name multiplied by any number of your choice as its value. 
# Print all the four variables Now add another variable to your program with any string of your choice. 
# Find its length, print its first and last character
#  and print a sub-string of this original string as well.

firstname="Jouri"
lastname="Alem"
fullname=firstname+lastname
result=fullname*5
str1="Hello World"

print("First name is ",firstname)
print("Last name is ",lastname)
print("Full name is ",fullname)
print("The full name tymes 5 is ",result)
print("str1 is ",str1)
print("Length of str1 is ",len(str1))
print("The first letter in str1 is ",str1[0])
print("The last letter in str1 is ",str1[-1])
#slicing
print("The sliced string is ",str1[1:5])
