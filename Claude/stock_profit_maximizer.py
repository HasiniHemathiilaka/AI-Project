def max_profit(prices):
    """Profit from the overall lowest and highest price in the list."""
    if len(prices) < 2:
        return 0
    profit = max(prices) - min(prices)
    return profit if profit > 0 else 0


def main():
    raw = input("Enter daily stock prices separated by spaces: ")
    parts = raw.split()

    try:
        prices = [float(p) for p in parts]
    except ValueError:
        print("Please enter numbers only, separated by spaces.")
        return

    if not prices:
        print("No prices entered.")
        return

    print(f"Prices: {prices}")
    print(f"Maximum profit: {max_profit(prices):g}")


if __name__ == "__main__":
    main()