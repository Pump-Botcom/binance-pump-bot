from binance.client import Client

# initialize the Binance client using your API key and secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
client = Client(api_key, api_secret)

# specify the symbol and quantity of the coin you want to buy
symbol = "BTCUSDT"
quantity = 0.01

# place the buy order
order = client.order_market_buy(
    symbol=symbol,
    quantity=quantity
)

print(order)
