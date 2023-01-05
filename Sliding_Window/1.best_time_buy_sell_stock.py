def maxProfit(prices):
    leftP = 0 
    rightP = 1
    profit = 0 

    while rightP < len(prices):
        if prices[leftP] > prices[rightP]: 
            leftP=rightP
            rightP+=1 
        else:
            print(f"buy: {prices[leftP]} sell: {prices[rightP]}")
            temp_profit = prices[rightP]-prices[leftP]
            if temp_profit > profit:
                profit = temp_profit
            rightP+=1
    return profit

prices = [2,1,2,1,0,1,2]

print(maxProfit(prices))

      
