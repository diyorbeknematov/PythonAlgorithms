class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = ''
        isTrue = True
        ind = 0
        minlen = min(strs, key=len)
        while isTrue and ind < len(minlen):
            current_char = minlen[ind]
            for x in strs:
                if current_char != x[ind]:
                    isTrue = False
                    break
            if isTrue:
                s += current_char
            ind += 1
                
        return s

test = Solution()
strs = ["flower", "flow", "flight"]
print(test.longestCommonPrefix(strs))
