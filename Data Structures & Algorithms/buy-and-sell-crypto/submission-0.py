class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr, maxi = float('inf'), 0
        profit = 0
        for price in prices:
            if curr > price:
                curr = price
            else:
                maxi = max(maxi, price-curr)
        return maxi