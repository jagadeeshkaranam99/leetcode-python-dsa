class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Determines whether any value appears at least twice in the array.

        Time Complexity: O(n) - Single pass using a hash set for O(1) lookups.
        Space Complexity: O(n) - Stores up to n unique elements in the set.
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
