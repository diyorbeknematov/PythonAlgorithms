class Solution:
    def isPalindrome(self, x: int) -> bool:
        son = 0
        y = x
        if x>=0:
            while x:
                son = son*10 + x%10
                x //=10
            return y==son
        else:
            return False 
test = Solution()

print(test.isPalindrome(121))