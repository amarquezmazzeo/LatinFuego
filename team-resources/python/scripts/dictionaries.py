# A Dictionary is used to hold a collection of key/value pairs,
# where each unique key has a value associated with it.

person = { 'Name': 'Clinton Daniel',
           'Gender': 'Male',
           'Occupation': 'Instructor',
           'Home City': 'Tampa' }

# Add a new key to the dictionary
person['Age'] = 46

print(person)

print(person['Name'])

vowels = {}
vowels['a'] = 0
vowels['u'] = 0
vowels['i'] = 0
vowels['e'] = 0
vowels['o'] = 0

# Increment a value in the dictionary
vowels['e'] = vowels['e'] + 1

# You can also increment this way
vowels['e'] += 1

print(vowels)
print('-- Iterate through a dictionary --')
# Iterate over the dictionary and process the keys
# NOTE: To access the associated data values, you need to put
# each key within square brakets and use it together with the
# dictionary name to gain access to the values associated with the key.
for key in vowels:
    print(key, 'was found', vowels[key], 'time(s).')

print('-- Sort a dictionary --')
# Use an iteration to return a sorted dictionary
for key in sorted(vowels):
    print(key, 'was found', vowels[key], 'time(s).')


print('-- Use the items method --')
# The items method can pass back tow loop variables
for key, value in sorted(vowels.items()):
    print(key, 'was found', value, 'time(s).')

