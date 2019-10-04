# Compute the sum of the first n integers algorithm using recursion
# sumFirstN function calls itself with a smaller value and has a base
# case that comes first. 
def sumFirstN(n):
    if n == 0:
        return 0
    
    return sumFirstN(n-1) + n

def main():
    x = int(input('Enter a number: '))

    s= sumFirstN(x)

    print('The sum of the first', x, 'integers are', str(s) + '.')

if __name__ == '__main__':
    main()
