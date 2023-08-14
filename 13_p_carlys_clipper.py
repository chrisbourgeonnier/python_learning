hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
  # find average haircut price
total_price = 0
for price in prices:
  total_price += price
  print(price, total_price)
average_price = total_price / len(prices)
print("")
print("Average Haircut Price: " + str(average_price))
  # lower each price by $5 with list comprehension
new_prices = [prices[i] - 5 for i in range(len(prices))]
print(new_prices)
  # find total revenues of the week
total_revenues = 0
for i in range(len(hairstyles)):
  total_revenues += prices[i] * last_week[i]
print(total_revenues)
  # find average daily revenue
average_daily_revenue = total_revenues / 7
print(average_daily_revenue)
  # select all cuts under $30 with list comprehension
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30] 
print(cuts_under_30)