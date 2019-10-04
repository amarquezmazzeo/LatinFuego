# Lists can dynamically shrink and grow to any size
# Objects are stored in individual slots in the list
# As with arrays, slots are numbered from zero upward - these are indexes
prices = []

temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]

words = ['hello', 'world']

car_details = ['Honda', 'Pilot', 2019, 3.7]

#Lists can be inside lists
odds_and_ends = [[1,2,3],['a','b','c'],['One','Two','Three']]

vowels = ['a','e','i','o','u']
word = "Milliways"

for letter in word:
    if letter in vowels:
        print(letter)

# Lists can grow
found = []
found.append('a')
found.append('i')
found.append('o')
print(found)
# Look for a value in a list, if it doesn't exist then add it
if 'u' not in found:
    found.append('u')
print(found)

# Remove objects from a list
found.remove('u')
print(found)

# Popping objects off a list
found.pop()
print(found)
found.pop(0)
print(found)

# Extending the list with objects
found.extend(['a','o'])
print(found)

# Inserting an object into a list
found.insert(0,'u')
print(found)

# Make a copy of a list using copy method
new_found = found.copy()
print(new_found)

