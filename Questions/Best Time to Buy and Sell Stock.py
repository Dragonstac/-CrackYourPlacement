def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        hold = -math.inf

        for i in prices:
            sell = max(sell, hold + i)
            hold = max(hold, -i)

        return sell