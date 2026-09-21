def max_profit(prices):
    """Maximum profit from one buy and one later sell. 0 if no profit exists."""
    min_price = float('inf')
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > best:
            best = price - min_price
    return best


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