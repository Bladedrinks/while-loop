# Program to work out the nth partial sum using for loop.

# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 4
# ...
# 1 + 2 + 3 + ... + n = the sum

n = int(input("Enter the last number you want to put into the nth partial sum: "))
the_sum = 0  # Initialize the variable which is used to store the nth partial sum.

# Each operand that takes part in the addition can be seen as a counter.
# And each time when we add a counter to the sum, the counter needs to be 1 greater than the last counter.
# Therefore, we need to provide the operation of addition with a new counter each time. This new counter
# can be picked from a "pool" (a numeric range) using a for loop.
for counter in range(1, n + 1):  # range(1, 11) generates integers from 0 up to, but not including. 11.
    the_sum += counter
print(f"The nth partial sum is: {the_sum}")
