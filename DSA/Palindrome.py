class Palindrome:
    def palindromeCheck(self, sttr: str, s: int, e: int) -> bool:
        def cal(self, sttr: str, s: int, e: int) -> bool:
            if s > e:
                print('s {}, e {}', (s,e))
                return False

            if sttr[s] != sttr[e]:
                print('{} {}', (sttr[s],sttr[e]))
                return False
            
            return cal(sttr, s+1, e-1)
        self.cal(sttr, s, e)
        

obj = Palindrome()
sttr = 'noodn'
obj.palindromeCheck(sttr, 0, len(sttr)-1)
