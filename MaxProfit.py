class MaxProfit():
    def maxProfit(self, prices):
        #Return 0 if null
        if not prices:
            return 0
        #Lowest starts at first day
        lowest = prices[0]
        highest = 0
        for i in range(len(prices)):
            #Profit for that day
            profit = prices[i] - lowest
            #Compare to highest profit
            if profit > highest:
                highest = profit
            #Update lowest if current index is lower
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