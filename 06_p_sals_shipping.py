weight = 41.5
shipping_cost = 0.00
if weight <=0:
    print("invalid weight")
else:
  # Ground Shipping
    flat_charge = 20.00
    flat_charge_premium = 125.00
    # Ground Shipping Cost Calculation
    if weight <= 2:
      cost = 1.50
      shipping_cost = cost * weight
    elif weight <= 6:
      cost = 3.00
      shipping_cost = cost * weight
    elif weight <= 10:
      cost = 4.00
      shipping_cost = cost * weight
    elif weight > 10:
      cost = 4.75
      shipping_cost = cost * weight
    print("Ground Shipping $ ", shipping_cost + flat_charge)
    # Ground Premium Shipping Cost Calculation
    print("Ground Shipping $ ", flat_charge_premium)
    # Drone Shipping Cost Calculation
    print("Ground Shipping $ ", shipping_cost * 3)


