def stockmax(prices):


    highest = prices[-1]
    profit = 0

    for i in range(len(prices)-1, -1, -1):
        if highest < prices[i]:
            highest = prices[i]
        profit += highest - prices[i]

    return profit
