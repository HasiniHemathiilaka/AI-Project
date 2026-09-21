def max_profit(prices):
    if not prices:
        return 0

    max_price = max(prices)
    min_price = min(prices)

    profit = max_price - min_price

    return profit if profit > 0 else 0


prices = list(map(int, input().split()))

print(max_profit(prices))




