# Program to create a list of geometric sequence made by multiplying by the same value (say, 3) each time.

# Initialize the list.
geo_seq = []

# Initialize the first term and the common ratio of the sequence.
# Let the first term be a and assign the user input to it.
a = int(input("Enter your first term: "))
# Let the common ratio be r (r is short for ratio) and assgin the user input to it.
r = float(input("Enter the common ratio: "))
print(f"The common ratio is {r}")
#
n = int(input("\nEnter the number of terms you expect: "))
while len(geo_seq) <= n:
    if a - int(a) == 0.0:
        a = int(a)
        geo_seq.append(a)
        a = a * r
    else:
        geo_seq.append(a)
        a = a * r
print(geo_seq)
