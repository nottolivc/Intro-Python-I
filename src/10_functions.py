# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    return num % 2 == 0


# Print out "Even!" if the number is even. Otherwise print "Odd"
print("Even!") if is_even(num) else print("Odd") 
