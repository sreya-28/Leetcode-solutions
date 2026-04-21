#best time to buy and sell stock
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ind=0
        mini=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
                ind=i
            elif prices[i]-mini>profit:
                profit=prices[i]-mini
        
        return profit
