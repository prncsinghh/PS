class Fibonacci:
    def calculate(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        ans2 = self.calculate(n-2)
        ans1 = self.calculate(n-1)

        return ans1 + ans2
    

obj = Fibonacci()
print(obj.calculate(3))




