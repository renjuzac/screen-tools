from stocks import stocks


high_growth  = stocks.get_stocks_with_revenue_growth_over("0.3")
volume_price = stocks.get_stock_price_and_vol([])

uniques = set(high_growth.keys()) & set(volume_price.keys())

for ticker in uniques:
    print ("{} {}  {}".format(ticker,volume_price[ticker],high_growth[ticker]))

print(len(uniques))
