#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        result = 0
        for i in range(1, len(prices)):
            if prices[i]-prices[i-1]>0:
                result += prices[i]-prices[i-1]
        return result

bar = Solution()
print(bar.maxProfit([1,3,5]))



