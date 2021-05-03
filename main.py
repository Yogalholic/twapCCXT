import ccxt
import schedule
import time
from random import seed
from random import randint
seed(2)
txMax = # choose a maximum size of the order, it should be an integer
txMin = # choose a minimum size of the order, it should be an integer
pauseMax = #choose the longest interval between two orders
pauseMin = #choose the shortest interval between two orders
exchange_id = '' #name of the exchange
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
        'apiKey': 'Key',
        'secret': 'Secret',
        # 'password': 'passphrase',#some exchanges ask for a passphrase
        'timeout': 30000,
        'enableRateLimit': True,
})
# exchange.set_sandbox_mode(True) #connect to sandbox
def return_bid(symbol):
        '''
        :param symbol: a trading pair ('BTC-USDT',...)
        :return: the second bid price in the orderbook
        '''
        exchange.load_markets(True)
        orderbook = exchange.fetch_l2_order_book (symbol,20)
        return orderbook['bids'][1][0]

symbol = 'BTC/USDT' #choose a trading pair

def launchtrade(symbol):
        bid = return_bid(symbol)
        try:
                order = exchange.create_limit_order(symbol, 'buy', randint(txMin, txMax), bid)
                print(order)
        except Exception as err:
                print(err)
schedule.every(randint(pauseMin, pauseMin)).minutes.do(launchtrade,symbol)
while True:
    schedule.run_pending()
    time.sleep(1)