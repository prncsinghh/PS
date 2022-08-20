def recursionSum(n):
    if n == 0:
        return 0
    else:
        return n + recursionSum(n - 1)


n = int(input())
if n < 0:
    print('Invalid number')
else:
    print(recursionSum(n))