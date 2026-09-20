
def max_profit(prices):
    # Find the overall minimum and maximum prices
    min_price = min(prices)
    max_price = max(prices)

    # Calculate the profit
    profit = max_price - min_price

    # Return 0 if no profit can be made
    if profit < 0:
        return 0

    return profit


# Main block
if __name__ == "__main__":
    # Get stock prices from the user
    user_input = input("Enter daily stock prices separated by spaces: ")

    # Convert input into a list of integers
    prices = list(map(int, user_input.split()))

    # Calculate maximum profit
    result = max_profit(prices)

    # Display the result
    print("Maximum profit:", result)


