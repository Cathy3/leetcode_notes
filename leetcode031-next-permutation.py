# -*- coding: utf-8 -*-
# Time:  O(n)
# Space: O(1)
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
#

class Solution:
    def nextPermutation(self,num):
        j, k = -1, 0 
        
        for i in range(len(num)-1):
            if num[i] < num[i+1]:
                j = i
        if j == -1:
            num.reverse()
            return 
        for i in range(j+1, len(num)):
            if num[i] > num[j]:
                k = i
        
        num[j], num[k] = num[k], num[j]
        num[j+1:] = num[:j:-1]

if __name__ == "__main__":
    num = [1,2,4,3,5]
    Solution().nextPermutation(num)
    print(num)
    Solution().nextPermutation(num)
    print(num)
    Solution().nextPermutation(num)
    print(num)
    Solution().nextPermutation(num)
    print(num)