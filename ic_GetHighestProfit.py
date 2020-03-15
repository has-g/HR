
def get_max_profit(stock_prices):
    # Returns 6 (buying for $5 and selling for $11)

    if len(stock_prices) == 0: return 0

    highestProfit = -1000000

    # walk through the list
    for i, buy in enumerate(stock_prices):
        # go to first element and walk right
        for sell in stock_prices[i+1:]:
            # work out positive difference
            profit = sell - buy

            # update highestProfit if lower
            if profit > highestProfit:
                highestProfit = profit

    return highestProfit

print(get_max_profit([9, 7, 4, 1]))
#print(get_max_profit([10, 7, 5, 8, 11, 9]))