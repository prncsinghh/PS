class Power:
    
    def calculate(self, x: int, n: int) -> int:
        if n == 0:
            return 1
        else:
            return x * self.calculate(x, n-1)

obj = Power()
print(obj.calculate(3, 5))


'''class Power:
    
    def calculate(self, x: int, n: int) -> int:
        total = 1
        for m in range(n):
            
            total = total * x
            
        return total

obj = Power()
print(obj.calculate(3, 2))
'''


'''
class Power:
    def calculate(self, x: int, n: int) -> int:
        return pow(x, n)

obj = Power()
print(obj.calculate(5, 5))
'''