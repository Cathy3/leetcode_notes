# -*- coding: utf-8 -*-
# Time:  O(n)
# Space: O(1)

# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.

# in-place solution

class Solution(object):
    def plusOne(self,digits):
        
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

if __name__ == "__main__":
    print(Solution().plusOne([9,9,9,9]))
    print(Solution().plusOne([0,0,0,0]))
    print(Solution().plusOne([1,2,3,4]))