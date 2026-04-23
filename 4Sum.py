#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# We can implement k - 2 loops using a recursion. We will pass the starting point and k as the parameters. When k == 2, we will call twoSum, terminating the recursion.
#
# For the main function:
#
# Sort the input array nums.
# Call kSum with start = 0, k = 4, and target, and return the result.
# For kSum function:
#
# At the start of the kSum function, we will check three conditions:
# Have we run out of numbers to choose from?
# Is the smallest number remaining greater than target / k?
# If so, then any k numbers we choose will be too large.
# Is the largest number remaining smaller than target / k?
# If so, then any k numbers we choose will be too small.
# If any of these conditions is true, there is no need to continue as no combination of the remaining elements can sum to target.
# If k equals 2, call twoSum and return the result.
# Iterate i through the array from start:
# If the current value is the same as the one before, skip it.
# Recursively call kSum with start = i + 1, k = k - 1, and target - nums[i].
# For each returned subset of values:
# Include the current value nums[i] into subset.
# Add subset to the result res.
# Return the result res.
# For twoSum function:
#
# Set the low pointer lo to start, and high pointer hi to the last index.
# While low pointer is smaller than high:
# If the sum of nums[lo] and nums[hi] is less than target, increment lo.
# Also increment lo if the value is the same as for lo - 1.
#     If the sum is greater than target, decrement hi.
# Also decrement hi if the value is the same as for hi + 1.
#     Otherwise, we found a pair:
# Add it to the result res.
# Decrement hi and increment lo.
# Return the result res.
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, K: int) -> List[List[int]]:
            res = []
            # If we have run out of numbers to add, return res.
            if not nums:
                return res
            # There re k remaining values to add to the sum. The average of these values is at least target //k.
            average_value = target // k
            # we cannot obtain a sum of target if the smallest value in nums is greatwe than target // k or if the largest vlue in nums is smaller than target //k.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in kSum(nums[i +1 :],target - nums[i], k-1):
                        res.append([nums[i]] + subset)
            return res
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi=0,len(nums) - 1
            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum > target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res
        nums.sort()
        return kSum(nums,target,4 )
