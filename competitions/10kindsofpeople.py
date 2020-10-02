# Store input

# create var name number_map
number_map = []

height, width = map(int, input().split()) # first line
for line in height:
     # map lines
     number_map.append(list(map(int, input().split())))
T = int(input()) # number of test cases

nodes = {}
# For each test case
for i in range(T):

    start_x, start_y, end_x, end_y = map(int, input().split())
    start_digit = number_map[start_x-1][start_y-1]
    end_digit = number_map[start_x-1][start_y-1]

    # If the digits of the end points are different, print 'neither' and break
    if start_digit !=  end_digit:
        print('neither')

    # If the digits are the same, then check if they are connected
    # If the endpoints were visited in a single test case before, that means they are connected (ignore for now)
    elif findPath():
        # If 1, then we are discarding binary (checking if 'decimal')
        if start_digit == 1:
            print('decimal')
        # If 0, then we are discarding decimal (checking if 'binary')
        elif start_digit == 0:
            print('binary')

    else print('neither')



def findPath():
    connection_found = False
    # TODO Write algorithm here
    return connection_found
            