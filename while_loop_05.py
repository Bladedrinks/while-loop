# Program to work out the nth partial sum of a number sequence with a common difference, using a while loop.
# Like: 1 + 3 + 5 + 7 + 9 + ... + n (where n % 2 != 0)

# Get n from the user:
n = int(input("Enter the last number you want to work out the partial sum ending with: "))
# Create and initialize a variable that will store the sum (that is, assign an initial value to the variable).
the_sum = 0
# To get the sum, we need to do an operation of addition.
# To complete the addition, we need to add an operand/counter to the latest sum.
counter = 1
# Since the operation of addition starts from 1, the first counter should be 1, not 0 or any other number.
common_difference = int(input("Enter the common difference of the number sequence: "))
while counter <= n:
    the_sum += counter
    counter += common_difference
print(f"The {n}th partial sum of odd numbers is: {the_sum}.")

