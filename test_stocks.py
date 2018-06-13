from stocks import stocks


def test_get_stocks_with_growth_over():

    assert type(stocks.get_stocks_with_revenue_growth_over("0.3")) == dict
    print(len(stocks.get_stocks_with_revenue_growth_over("0.1")))
    assert (len(stocks.get_stocks_with_revenue_growth_over("0.1")) > 0) == True
