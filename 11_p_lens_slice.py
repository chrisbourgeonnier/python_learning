  # create a list of toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
  # create a list of prices
prices = [2, 6, 1, 3, 2, 7, 2]
  # count the number of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
  # find the number of kinds of pizzas
num_pizzas = len(toppings)
print("We sell ", num_pizzas, " different kinds of pizza!")
  # new list
pizza_and_prices = [[2, "pepperoni"], [2, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
  # sort pizzas by ascending price
pizza_and_prices.sort()
print(pizza_and_prices)
  # find the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
  # find the priciest pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
  # remove the priciest
pizza_and_prices.pop()
print(pizza_and_prices)
  # add a new "peppers" pizza
pizza_and_prices.insert(5, [2.5, "peppers"])
print(pizza_and_prices)
  # the three cheapest pizzas
three_cheapest= pizza_and_prices[:3]
print(three_cheapest)