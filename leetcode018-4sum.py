# -*- coding: utf-8 -*-

# Time:  O(n^3)
# Space: O(1)

# Given an array S of n integers,
# are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order.
# (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
#   A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)
#

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        
        for i in range(len(nums)-3):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                
                sum = target - nums[i] - nums[j]
                left, right = j+1, len(nums)-1
                
                while left < right:
                    if nums[left] + nums[right] == sum:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return result
                        
if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))                       