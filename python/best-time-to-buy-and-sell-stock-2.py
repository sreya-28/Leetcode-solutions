#best time to buy and sell stock-2
#difficulty: medium
#language: python
#link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total=0
        for i in range(1,len(prices)):
            
            if prices[i]>prices[i-1]:
                total+=prices[i]-prices[i-1]
        return total
