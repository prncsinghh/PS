class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPalindromeHelper(l, r, s):
            if l >= r:
                return False
            
            if s[l] != s[r]:
                return False
            
            return isPalindromeHelper(l+1, r-1, s)

charString = 'nfsjf'
ans = isPalindromeHelper(0, len(charString)-1, charString)
return print(ans)

obj = Solution()
obj.isPalindrome(charString)


