stock_prices = [10, 7, 5, 8, 11, 9]
stock_prices = [10, 7, 8, 11, 5, 9]
stock_prices = [10, 7, 5, 8, 11, 12]
#stock_prices = [10, 7, 5, 8, 11, 9]
#stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices):
    # Returns 6 (buying for $5 and selling for $11)
    lowest_price = stock_prices[0]
    max_profit = 0
    for item in stock_prices:
            print('>>' + str(item))

            # calculate positive profit, if negative then set low_price to new value
            sale_value = item - lowest_price
            if (sale_value > max_profit):
                max_profit = sale_value
                print('max profit = ' + str(max_profit))
            if (item < lowest_price):
                lowest_price = item
                print('new low value found = ' + str(item))

    return max_profit

print(get_max_profit(stock_prices))