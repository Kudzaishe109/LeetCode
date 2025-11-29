class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final = []
        for i in range(len(prices) - 1):
            discount = 0
            for price in prices[i+1:]:
                if price <= prices[i]:
                    discount = price
                    break 
            final.append(prices[i] - discount)
        final.append(prices[-1])
        return final
