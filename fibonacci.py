fibonacci_sequence = []

a = 0
b = 1
fibonacci_sequence.append(a)
fibonacci_sequence.append(b)

print(fibonacci_sequence)

# Ask the user for the index
index = int(input("What index would you like to see? "))

# Loop to generate the Fibonacci sequence up to the requested index
for i in range(2, index):  # Start from 2 since the first two numbers are already in the list
    new_num = sum(fibonacci_sequence[-2:])  # Sum the last two elements
    fibonacci_sequence.append(new_num)  # Append the new number to the sequence

# Show the final sequence up to the requested index
print(fibonacci_sequence)
