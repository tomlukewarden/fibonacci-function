fibonacci_sequence = []

a = 0
b = 1
fibonacci_sequence.append(a)
fibonacci_sequence.append(b)

print(fibonacci_sequence)
index=input("What index would you like to see? ")
# If you want to calculate a new number as the sum of the last two numbers
# We can use slicing to sum the last two elements.
for i in range(index):
    new_num = sum(fibonacci_sequence[-2:])  # Slicing to get the last two elements
print(new_num)

fibonacci_sequence.append(new_num)  # Add the new number to the sequence
print(fibonacci_sequence)