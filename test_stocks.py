from stocks import stocks


def test_get_stocks_with_growth_over():

    res = stocks.get_stocks_with_revenue_growth_over("0.3")
    print(type(res))
#    print(res)
    pass