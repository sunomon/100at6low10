import time
import pyupbit
import datetime
import schedule
from fbprophet import Prophet

access = "PgXnWWPxxv88s7z2PSnz4aoqaYL0gxkRxReK0WDK"
secret = "wgCfiEmQVH76s9sblwFKQsOKOp91t2ic3XAHuNsK"

def get_target1_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target1_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target1_price

def get_target2_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target2_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target2_price

def get_target3_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target3_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target3_price

def get_target4_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target4_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target4_price

def get_target5_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target5_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target5_price

def get_target6_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target6_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target6_price

def get_start_time(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

predicted_close_price = 0
def predict_price(ticker):
    global predicted_close_price
    df = pyupbit.get_ohlcv(ticker, interval="minute60")
    df = df.reset_index()
    df['ds'] = df['index']
    df['y'] = df['close']
    data = df[['ds','y']]
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    closeDf = forecast[forecast['ds'] == forecast.iloc[-1]['ds'].replace(hour=9)]
    if len(closeDf) == 0:
        closeDf = forecast[forecast['ds'] == data.iloc[-1]['ds'].replace(hour=9)]
    closeValue = closeDf['yhat'].values[0]
    predicted_close_price = closeValue
predict_price("KRW-CBK")
schedule.every().hour.do(lambda: predict_price("KRW-CBK"))

upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-CBK")
        middle1_time = start_time + datetime.timedelta(hours=3)
        middle2_time = start_time + datetime.timedelta(hours=9)
        middle3_time = start_time + datetime.timedelta(hours=15)
        end_time = start_time + datetime.timedelta(days=1)
        schedule.run_pending()

        if start_time < now < end_time - datetime.timedelta(hours=1):
            target1_price = get_target1_price("KRW-CBK", 0.1)
            target2_price = get_target2_price("KRW-CBK", 0.2)
            target3_price = get_target3_price("KRW-CBK", 0.3)
            target4_price = get_target4_price("KRW-CBK", 0.4)
            target5_price = get_target5_price("KRW-CBK", 0.5)
            target6_price = get_target6_price("KRW-CBK", 0.6)
            current_price = get_current_price("KRW-CBK")
            krw = get_balance("KRW")
            cbk = get_balance("CBK")
            if target1_price <= current_price < target1_price*1.02 and target1_price*1.1 <= predicted_close_price:
                if krw >= 1000000 and cbk < 10000/(target1_price*1.02):
                    upbit.buy_market_order("KRW-CBK", 1000000)
                if 5000 < krw < 1000000 and cbk < 10000/(target1_price*1.02):
                    upbit.buy_market_order("KRW-CBK", krw*0.9995)
            if target2_price <= current_price < target2_price*1.02 and target2_price*1.15 <= predicted_close_price:
                if krw >= 1000000 and cbk < 10000/(target2_price*1.02):
                    upbit.buy_market_order("KRW-CBK", 1000000)
                if 5000 < krw < 1000000 and cbk < 10000/(target2_price*1.02):
                    upbit.buy_market_order("KRW-CBK", krw*0.9995)
            if target3_price <= current_price < target3_price*1.02 and target3_price*1.2 <= predicted_close_price:
                if krw >= 1000000 and cbk < 10000/(target3_price*1.02):
                    upbit.buy_market_order("KRW-CBK", 1000000)
                if 5000 < krw < 1000000 and cbk < 10000/(target3_price*1.02):
                    upbit.buy_market_order("KRW-CBK", krw*0.9995)
            if target4_price <= current_price < target4_price*1.02 and target4_price*1.25 <= predicted_close_price:
                if krw >= 1000000 and cbk < 10000/(target4_price*1.02):
                    upbit.buy_market_order("KRW-CBK", 1000000)
                if 5000 < krw < 1000000 and cbk < 10000/(target4_price*1.02):
                    upbit.buy_market_order("KRW-CBK", krw*0.9995)
            if target5_price <= current_price < target5_price*1.02 and target5_price*1.3 <= predicted_close_price:
                if krw >= 1000000 and cbk < 10000/(target5_price*1.02):
                    upbit.buy_market_order("KRW-CBK", 1000000)
                if 5000 < krw < 1000000 and cbk < 10000/(target5_price*1.02):
                    upbit.buy_market_order("KRW-CBK", krw*0.9995)
            if target6_price <= current_price < target6_price*1.02 and target6_price*1.35 <= predicted_close_price:
                if krw >= 1000000 and cbk < 10000/(target6_price*1.02):
                    upbit.buy_market_order("KRW-CBK", 1000000)
                if 5000 < krw < 1000000 and cbk < 10000/(target6_price*1.02):
                    upbit.buy_market_order("KRW-CBK", krw*0.9995)
            if cbk > 1000000*1.001*1.2/current_price:
                upbit.sell_market_order("KRW-CBK", cbk*0.9995)  
        elif middle1_time < now < middle2_time:
            cbk = get_balance("CBK")
            current_price = get_current_price("KRW-CBK")
            if cbk > 1000000*1.001*1.1/current_price:
                upbit.sell_market_order("KRW-CBK", cbk*0.9995)  
        elif middle2_time < now < middle3_time:
            cbk = get_balance("CBK")
            current_price = get_current_price("KRW-CBK")
            if cbk > 1000000*1.001*1.05/current_price:
                upbit.sell_market_order("KRW-CBK", cbk*0.9995)  
        elif middle3_time < now < end_time - datetime.timedelta(hours=1):
            cbk = get_balance("CBK")
            current_price = get_current_price("KRW-CBK")
            if cbk > 1000000*1.001*1.03/current_price or current_price > predicted_close_price:
                upbit.sell_market_order("KRW-CBK", cbk*0.9995)  
        else:
            cbk = get_balance("CBK")
            current_price = get_current_price("KRW-CBK")
            if cbk > 1000000*1.001/current_price:
                upbit.sell_market_order("KRW-CBK", cbk*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
