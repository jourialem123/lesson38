# Store your Name, Age, Weight, Whether you are a student or not (True for yes, False for no) in respective variables.
#  What do you think is the data type of each variable?
#  Print the data type of every variable.
#  Change the datatype of Age to string and Weight to an integer.

name="Jouri"
age=16
weight=30.5
isstudent=True

print("data type of name before type casting is ",type(name))
print("data type of age before type casting is ",type(age))
print("data type of weight before type casting is ",type(weight))
print("data type of is student before type casting is ",type(isstudent))

name=str(name)
weight=int(weight)

print("data type of name after type casting is ",type(name))
print("data type of weight after type casting is ",type(weight))