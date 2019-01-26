# Program to work out the nth partial sum (1 + 2 + 3 + 4 + ... + n) using the
# while loop.

# n could be any positive natural number that the user offers.
n = int(input("Enter your n: "))

# The nth partial sum can also be called "triangular number".

# Any operation of addition of numbers needs a jumping-off point
# or an initial value. So we need to assign an initial value to the variable
# that will contain the nth partial sum and the variable that, as a counter,
# will help the addition go on and on until the nth operand is added.
# The counter is changing as the addition goes from 1 to n (1, 2, 3, 4, 5, 6, ..., 10 if n is 10).
# In other words, the counter represents each one of operands that take part in the addition.
# counter = 1, and then counter = 2, and then counter = 3, and then counter = 4,
# and then ... and then counter = n - 1, and then counter = n.
tri_num = 0
counter = 1

while counter <= n:   # If the n is 10, then the greatest value of the counter is 10.
    tri_num += counter
    # The final result (the sum) is:
    # the sum of the (n-1)th partial sum and the final counter/operand (= n).
    counter += 1
    # After one iteration, the next iteration needs to be 1 greater than the last counter.
    # For example, 2 is 1 greater than 1. 3 is 1 greater than 2. 4 is 1 greater than 3.
print(f"The triangular number is equal to {tri_num}.")
