import ccxt
import config
# bitfinex = ccxt.bitfinex({
#     'apiKey': config.loginBitfinex,
#     'secret': config.passBitfinex,
#     'timeout': 30000,
#     'enableRateLimit': True,
# }) # default id
# kucoin = ccxt.kucoin({
#     'apiKey': config.Key,
#     'secret': config.Secret,
#     'password': config.passphrase,
#     'timeout': 30000,
#     'enableRateLimit': True,
# }) # default
# from variable id
exchange_id = 'kucoin'
exchange_class = getattr(ccxt, exchange_id)
kucoin = exchange_class({
        # 'set_sandbox_mode': True,
        'apiKey': config.Key,
        'secret': config.Secret,
        'password': config.passphrase,
        'timeout': 30000,
        'enableRateLimit': True,
})
kucoin.set_sandbox_mode(True)
balance = kucoin.fetch_balance()
print(balance)
# okcoin1 = ccxt.okcoinusd ({ 'id': 'okcoin1' })
# id = 'btcchina'
# btcchina = eval ('ccxt.%s ()' % id)
# coinbasepro = getattr (ccxt, 'coinbasepro') ()

# # from variable id
# exchange_id = 'kucoin'
# exchange_class = getattr(ccxt, exchange_id)
# exchange = exchange_class({
#     'apiKey': 'YOUR_API_KEY',
#     'secret': 'YOUR_SECRET',
#     'timeout': 30000,
#     'enableRateLimit': True,
# })