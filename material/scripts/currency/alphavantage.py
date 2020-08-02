import json
import urllib.request

# docs https://www.alphavantage.co/documentation/
# get your own key here https://www.alphavantage.co/support/#api-key
API_KEY = '0DIY2G95J96HJ9UK'

# physical currency
currency_brl = 'BRL'  # Brazilian Real
currency_cad = 'CAD'  # Canadian Dollar
currency_cny = 'CNY'  # Chinese Yuan
currency_jpy = 'JPY'  # Japanese Yen
currency_usd = 'USD'  #United States Dollar

# digital currency
currency_bat = 'BAT'  # Basic-Attention-Token
currency_bch = 'BCH'  # Bitcoin-Cash
currency_bcn = 'BCN'  # Bytecoin
currency_btc = 'BTC'  # Bitcoin
currency_etc = 'ETC'  # Ethereum-Classic
currency_eth = 'ETH'  # Ethereum
currency_xmr = 'XMR'  # Monero

func_exchange = 'CURRENCY_EXCHANGE_RATE'


def getdata(alpha_func, from_currency, to_currency, api=API_KEY):
    url = f'''https://www.alphavantage.co/query?function={alpha_func}&from_currency={from_currency}&to_currency={to_currency}&apikey={api}'''
    data = json.loads(urllib.request.urlopen(url).read())
    try:
        return float(
            data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    except Exception:
        pass


alpha_data_usd = getdata(func_exchange, currency_usd, currency_brl)
print(f'${alpha_data_usd:,.2f}')
