# given a list of numbers,
# find the best time to buy, and the best time to sell,
# if numbers keep going down, dont buy at all,
def get_max_profit(stock_prices):
# TELL USER they need at least 2 numbers!!!
  if len(stock_prices) < 2:
    raise ValueError("need at least 2 numbers!!")

  max_profit = stock_prices[1] - stock_prices[0]
  min_price = stock_prices[0]
  
  for current_index in range(1, len(stock_prices)):
    current_price = stock_prices[current_index]
    profit = current_price - min_price
    max_profit = max(profit, max_profit)
    min_price = min(current_price, min_price)

  return max_profit

print(get_max_profit([100, 60, 40, 10, 5]))
# print(get_max_profit([5]))


# O(n^2) time complexity, O(n) space complexity

# O(n) in time complexity, O(1) space complexity