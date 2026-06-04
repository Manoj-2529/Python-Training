print("Welcome to Domino's Online Pizza Delivery System")

num_pizzas = int(input("Enter Number of Pizzas: "))
grand_total = 0

for n in range(num_pizzas):
    print(f"\nPizza {n+1}")

    size = input("Enter Pizza Size (small/medium/large): ")

    if size == "large":
        pizza_price = 20
    elif size == "medium":
        pizza_price = 15
    elif size == "small":
        pizza_price = 12
    else:
        print("Invalid Size Selection")
        continue

    toppings = int(input("Enter Number of Toppings: "))
    total_price=0

    for i in range(toppings):
        topping = input(f"Enter Topping {i+1} (cheese/pepperoni/olives/jalapeno): ")
        if topping == "cheese":
            total_price = total_price +  2
        elif topping == "pepperoni":
            total_price = total_price +  3
        elif topping == "olives":
            total_price = total_price +  5
        elif topping == "jalapeno":
            total_price = total_price +  5
        else:
            print("Invalid Topping")

    print("Pizza Price: $", total_price)
    grand_total += total_price + pizza_price
if grand_total < 50:
    delivery_charge = 5
else:
    delivery_charge = 0

final_bill = grand_total + delivery_charge

print("\n------ BILL ------")
print("Order Total: $", grand_total)
print("Delivery Charge: $", delivery_charge)
print("Final Bill: $", final_bill)
print("Thank you for ordering!")