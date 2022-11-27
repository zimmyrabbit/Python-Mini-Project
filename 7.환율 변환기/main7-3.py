from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_exchange_rate(target1,target2):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        , 'Content-Type': 'text/html; charset=utf-8'
    }

    url = Request("https://kr.investing.com/currencies/{}-{}".format(target1,target2), headers=headers)
    html = urlopen(url)
    content = BeautifulSoup(html, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    print(containers.text)

get_exchange_rate('usd','krw')