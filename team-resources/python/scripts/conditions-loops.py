# Demonstrates the for loop
for i in [1,2,3,4,5]:
    print(i)

# Iterate through the string one character at a time
for ch in "Hello World!":
    print(ch)

# Iterate a specific number of times
for num in range(5):
    print("Python is fun!")

# Generate random integers
import random
# Display all the attributes, or you can run this from the Python command prompt
print(dir(random))
# Ask the interpreter for help, run this from the Python command prompt
print(help(random.randint))
# Print a random number between 1 and 60
print(random.randint(1,60))

# Return a sequence of numbers from start to stop by step using Range
word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")

if beer_num == 1:
    print("No more bottles of beer on the wall.")
else:
    new_num = beer_num -1
    if new_num == 1:
        word = "bottle"
    print(new_num,word, "of beer of the wall.")



