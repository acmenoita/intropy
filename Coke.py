# Set the cost of a Coke bottle
cost = 50
add_money = cost

# Loop until the user has inserted enough coins
while add_money > 0:
    # Inform the user how much is due and prompt for a coin
    print(f"Add money: {add_money} cents")
    coin = int(input("Insert coin: "))

    # Check if the inserted coin is valid (5, 10, or 25 cents)
    if coin in [25, 10, 5]:
        add_money -= coin
    else:
        # Ignore invalid coins and continue prompting
        print("Invalid coin")

# Calculate the change (if any) once add_money is 0 or less
change = abs(add_money)
print(f"Change owed: {change} cents")