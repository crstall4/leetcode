#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s:
            number += translations[char]

        return number


        # my gross solution:
        # output = 0
        # output += s.count('IV')*4
        # output += s.count('IX')*9
        # output += s.count('XL')*40
        # output += s.count('XC')*90
        # output += s.count('CD')*400
        # output += s.count('CM')*900
        # s = s.replace('IX','')
        # s = s.replace('XL','')
        # s = s.replace('XC','')
        # s = s.replace('CD','')
        # s = s.replace('IV','')
        # s = s.replace('CM','')

        # output += s.count('I')
        # output += s.count('V')*5
        # output += s.count('X')*10
        # output += s.count('L')*50
        # output += s.count('C')*100
        # output += s.count('D')*500
        # output += s.count('M')*1000

        # return output

# @lc code=end

