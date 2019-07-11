# given a list of numbers,
# find the best time to buy, and the best time to sell,
# if numbers keep going down, dont buy at all,

def get_max_profit(stock_prices):
  max_profit = 0

  list_profits = list()

  for currentIndex in range(len(stock_prices) - 1):
    for currentIndex2 in range (currentIndex + 1, len(stock_prices)):
      currentProfit = stock_prices[currentIndex2] - stock_prices[currentIndex]
      list_profits.append(currentProfit)

  max_profit = max(list_profits)
  
  return max_profit

print(get_max_profit([55,66,77,44]))
# print(get_max_profit([55,66,77,44]))


# O(n^2) time complexity, O(n) space complexity

# O(n) in time complexity, O(1) space complexity