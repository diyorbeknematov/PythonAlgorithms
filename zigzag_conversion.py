class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>len(s):
            return s
        
        lst = [[] for row in range(numRows)]
        ind = 0
        step = 1

        for i in s:
            lst[ind].append(i)
            if ind==0:
                step = 1
            elif ind == numRows-1:
                step = -1
            ind += step
        
        for i in range(numRows):
            lst[i]=''.join(lst[i])
        return ''.join(lst)

test = Solution()

print(test.convert("paypalishiring", 4))