# given a list of numbers,
# find the best time to buy, and the best time to sell,
# if numbers keep going down, dont buy at all,

def get_max_profit(stock_prices):
  for current in range(len(stock_prices)):
    print(stock_prices[current])

  max_profit = 18
  return max_profit

get_max_profit([55,66,77,44])