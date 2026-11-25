class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Finds the maximum profit from a single buy and sell transaction.

        Time Complexity: O(n) - Single pass through the prices array.
        Space Complexity: O(1) - Constant extra space used.
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
