class Solution:
    def intToRoman(self, num: int) -> str:
        s=''
        intTostr = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        keys = [key for key in intTostr.keys()]
        keys.sort(reverse=True)

        while num:
            for key in keys:
                x = num//key
                s += intTostr[key]*x
                num %=key
        return s
test = Solution()
print(test.intToRoman(900))