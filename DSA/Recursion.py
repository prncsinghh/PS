# this function will return the recursion
def fac(n):
    if n == 0:
        return 1
    #recursion call
    else:
        return n * fac(n-1)

n = int(input())
if n < 0:
    print('Invalid number')
else:
    print(fac(n))






























'''


def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

n = int(input())
if n < 0:
    print('Invalid number')
else:
    print(fac(5))

'''

'''
def recursion(n):
    total = n
    while n > 1:
        print('n: ',n)
        total = total * (n-1)
        n = n - 1
    print('Factorial: ', total)
recursion(5)
'''