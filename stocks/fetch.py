import requests
import json
import requests_cache
from datetime import timedelta

from config import username,password

expire_after = timedelta(hours=1)
requests_cache.install_cache('stocks/api_cache', expire_after=expire_after)


ticker = "NTNX"
#url = "https://api.intrinio.com/companies?ticker={}".format(ticker)
#url2 = "https://api.intrinio.com/data_point?identifier={}&item=revenuegrowth".format(ticker)
#url3 = "https://api.intrinio.com/securities/search?conditions=revenuegrowth~gt~0.3"
#url4 = "https://api.intrinio.com/data_point?identifier={}&item=volume".format(ticker)
# FULL URL: https://api.intrinio.com/data_point?identifier=GOOGL,AAPL&item=price_date,close_price,percent_change

#response = requests.get(url3, auth=(username, password))
#print(response.text)
#print(response.headers)
#print(response.json())

def get_url(url):
    try:
        response = requests.get(url, auth=(username, password))
        results = json.loads(response.text)
        return results

    except Exception as e:
        print("Error fetching data from server :- {}".format( base_url))
        print ("Response string:{}".format(response.text))
        return {}





def get_stocks_with_revenue_growth_over(percent ):
    ''' e.g.  percent="0.3"  (is 30% )
    API returns first 150 by default
    API e.g.  'result_count': 714, 'page_size': 100, 'current_page': 1, 'total_pages': 8,'''
    page_number = 1
    total_pages = 1
    base_url = "https://api.intrinio.com/securities/search?conditions=revenuegrowth~gt~{}&page_number={}"
    try:
        stocks = {}
        while page_number <= total_pages:
            search_url = base_url.format(percent, page_number)
            results = get_url(search_url)
            total_pages = results["total_pages"]
            for item in results["data"]:
                stocks.update({item['ticker'] :item['revenuegrowth']})
            page_number += 1

        return stocks

    except Exception as e:
        print ("{}Error fetching data from server {}".format(e,base_url))
        return {}

def get_stock_price_and_vol(stock_list):
    base_url = "https://api.intrinio.com/securities/search?conditions=close_price~gt~15,average_daily_volume~gt~1000000&page_number={}"

    page_number = 1
    total_pages = 1
    stocks = {}
    while page_number <= total_pages:
        search_url = base_url.format(page_number)
        results = get_url(search_url)
        total_pages = results["total_pages"]
        for item in results["data"]:
            stocks.update({item['ticker']: item['close_price']})
        page_number += 1

    return stocks




