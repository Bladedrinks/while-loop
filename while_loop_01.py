# Program to add natural numbers (starting from 1) to get
# the sum (sum = 1 + 2 + 3 + ... + n).

# Take input from the user.
n = int(input("n = "))

# Initialize sum and counter (that is, to assign initial
# values to sum and counter)
# A counter is a variable whose contents are incremented to keep a count.
SUM = 0
# Initialize the variable "sum". That is, to assign the initial
# value to the variable "sum".
counter = 1
# Initialize the variable "counter". That is, to assign the initial value
# to the variable "counter". The variable "counter" is used to help keep
# the counting go on and on by adding itself to the sum.

while counter <= n:
    SUM = SUM + counter
    counter = counter + 1  # Update the counter

# The whole activity of repeating executing the body of while loop is shown below:

# sum                         = 0
# counter                       = 1

# sum   counter
# 0     1
# sum = sum + counter = 0 + 1 = 1
# counter = counter + 1 = 1 + 1 = 2

# sum   counter
# 1     2
# sum = sum + counter = 1 + 2 = 3
# counter = counter + 1 = 2 + 1 = 3

# sum   counter
# 3     3
# sum = sum + counter = 3 + 3 = 6
# counter = counter + 1 = 3 + 1 = 4

# sum   counter
# 6     4
# sum = sum + counter = 6 + 4 = 10
# counter = counter + 1 = 4 + 1 = 5

# sum   counter
# 10    5
# sum = sum + counter= 10 + 5 = 15
# counter = counter + 1 = 5 + 1 = 6

# sum   counter
# 15    6
# sum = sum + counter= 15 + 6 = 21
# counter = counter + 1 = 6 + 1 = 7

# sum   counter
# 21    7
# sum = sum + counter= 21 + 7 = 28
# counter = counter + 1 = 7 + 1 = 8

# sum   counter
# 28    8
# sum = sum + counter= 28 + 8 = 36
# counter = counter + 1 = 8 + 1 = 9

# sum   counter
# 36    9
# sum = sum + counter= 36 + 9 = 45
# counter = counter + 1= 9 + 1 = 10

# sum   counter
# 45    10
# sum = sum + counter=45 + 10 = 55
# counter =counter + 1= 10 + 1 = 11

print("The sum is", SUM)

