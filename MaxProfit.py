class MaxProfit():
    def maxProfit(self, prices):
        if not prices:
            return 0
        lowest = prices[0]
        highest = 0
        for i in range(len(prices)):
            profit = prices[i] - lowest
            if profit > highest:
                highest = profit
            if prices[i] < lowest:
                lowest = prices[i]
        return highest
    
test1 = [1,7,10,4]
test2 = [7,90,5,4]

mp = MaxProfit()

result1 = mp.maxProfit( test1)
result2 = mp.maxProfit(test2)

print(result1)
print(result2)