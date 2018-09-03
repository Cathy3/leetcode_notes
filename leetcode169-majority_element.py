# -*- coding: utf-8 -*-


# Time:  O(n)
# Space: O(1)
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [n/2] times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    def majorityElement(self, nums):
        idx, cnt = 0,1
        
        for i in range(1,len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1
        return nums[idx]

if __name__  == "__main__":
    print(Solution().majorityElement([2,3,4,5,6,5,5,5,5,4]))