# -*- coding: utf-8 -*-

# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element
# is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#

class Solution:
    def maxProfit(self, prices):
        minprice, maxprofit = float("inf"), 0
        
        for price in prices:
            minprice = min(minprice ,price)
            maxprofit = max(maxprofit, price-minprice)
        return maxprofit
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
