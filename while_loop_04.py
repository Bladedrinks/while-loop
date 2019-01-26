# Program to work out the nth partial sum of odd numbers, using a while loop.
# Like: 1 + 3 + 5 + 7 + 9 + ... + n (where n % 2 != 0)

# Get n from the user:
n = int(input("Enter the last odd number you want to work out the partial sum ending with: "))
if n % 2 == 1:
    # Create and initialize a variable that will store the sum (that is, assign an initial value to the variable).
    the_sum = 0
    # To get the sum, we need to do an operation of addition.
    # To complete the addition, we need to add an operand/counter to the latest sum.
    # Each operand is 2 greater than the last one.
    # For example, 3 is 2 greater than 1. 5 is 2 greater than 3. 7 is 2 greater than 5, etc.
    # Create and initialize a variable that is used as a counter.
    counter = 1
    # Since the operation of addition starts from 1, the first counter should be 1, not 0 or any other number.
    while counter <= n:
        the_sum += counter
        counter += 2
        # Since the common difference between each operand is 2 (eg. 3 - 1 = 5 - 3 = 2), we put 2 in this += assignment.
    print(f"The {n}th partial sum of odd numbers is: {the_sum}.")
else:
    print('''
    -------------------------------------------------------------------
     Hey, only an odd number is needed! Don't make me freak out again.
    -------------------------------------------------------------------
    ''')
