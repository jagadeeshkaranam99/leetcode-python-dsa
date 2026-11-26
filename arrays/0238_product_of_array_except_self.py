class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Calculates the product of all elements except self without using division.

        Time Complexity: O(n) - Two linear passes (prefix and suffix products).
        Space Complexity: O(1) - Extra space excluding the output array.
        """
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
