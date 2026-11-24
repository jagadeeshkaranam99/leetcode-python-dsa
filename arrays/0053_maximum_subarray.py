class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Finds the contiguous subarray with the largest sum using Kadane's Algorithm.

        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(1) - Constant extra space used.
        """
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
