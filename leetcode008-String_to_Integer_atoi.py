# -*- coding: utf-8 -*-
# Time:  O(n)
# Space: O(1)
#
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below
# and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that
# form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#

class Solution(object):
    def myAtoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = 0
        
        if not str:
            return result
        i = 0
        while i < len(str) and str[i].isspace():
            i += 1
        
        if i == len(str):
            return result
        
        sign = 1
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        
        while i < len(str) and '0' <= str[i] <= '9':
            if result > (INT_MAX -int(str[i]))/10:
                return INT_MAX if sign > 0 else INT_MIN
            result = result * 10 + int(str[i])
            i += 1
        
        return sign * result
    
if __name__ == "__main__":
    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("   -42"))
    print(Solution().myAtoi("words and 987"))

            