class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [-1] * n
        def dfs(i, buy, summ):
            if i == n-1:
                return summ+prices[i]-buy if buy != -1 and prices[i] > buy else summ
            elif i >= n:
                return summ
                
            ret = -1
             # Skip the current day altogether
            print(f'i: {i}, buy: {buy}, summ: {summ}')
            ret = max(ret, dfs(i+1, buy, summ))

            if buy == -1: # Buy current day, then skip a day
                print(f'i: {i}, buy: {buy}, summ: {summ}')
                ret = max(ret, dfs(i+1, prices[i], summ))

            elif prices[i] > buy: # Sell coin
                print(f'i: {i}, buy: {buy}, summ: {summ}')
                ret = max(ret, dfs(i+2, -1, summ+prices[i]-buy))

            return ret
            
        return dfs(0, -1, 0)