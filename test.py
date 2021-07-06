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

def get_target7_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target7_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target7_price

def get_target8_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target8_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target8_price

def get_target9_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target9_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target9_price

def get_target10_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target10_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target10_price

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
predict_price("KRW-ADA")
schedule.every().hour.do(lambda: predict_price("KRW-ADA"))

upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ADA")
        middle1_time = start_time + datetime.timedelta(hours=3)
        middle2_time = start_time + datetime.timedelta(hours=9)
        middle3_time = start_time + datetime.timedelta(hours=15)
        end_time = start_time + datetime.timedelta(days=1)
        schedule.run_pending()

        if start_time < now < end_time - datetime.timedelta(hours=1):
            target1_price = get_target1_price("KRW-ADA", 0.1)
            target2_price = get_target2_price("KRW-ADA", 0.2)
            target3_price = get_target3_price("KRW-ADA", 0.3)
            target4_price = get_target4_price("KRW-ADA", 0.4)
            target5_price = get_target5_price("KRW-ADA", 0.5)
            target6_price = get_target6_price("KRW-ADA", 0.6)
            target7_price = get_target7_price("KRW-ADA", 1)
            target8_price = get_target8_price("KRW-ADA", 1.5)
            target9_price = get_target9_price("KRW-ADA", 2)
            target10_price = get_target10_price("KRW-ADA", 3)
            current_price = get_current_price("KRW-ADA")
            krw = get_balance("KRW")
            ada = get_balance("ADA")
            if target1_price <= current_price < target1_price*1.02 and target1_price*(0.807) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target1_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target1_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target2_price <= current_price < target2_price*1.02 and target2_price*(0.824) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target2_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target2_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target3_price <= current_price < target3_price*1.02 and target3_price*(0.843) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target3_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target3_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target4_price <= current_price < target4_price*1.02 and target4_price*(0.863) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target4_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target4_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target5_price <= current_price < target5_price*1.02 and target5_price*(0.883) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target5_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target5_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target6_price <= current_price < target6_price*1.02 and target6_price*(0.905) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target6_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target6_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target7_price <= current_price < target7_price*1.02 and target7_price*(1) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target7_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target7_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target8_price <= current_price < target8_price*1.02 and target8_price*(1.13) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target8_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target8_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target9_price <= current_price < target9_price*1.02 and target9_price*(1.27) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target9_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target9_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)
            if target10_price <= current_price < target10_price*1.02 and target10_price*(1.58) <= predicted_close_price:
                if krw >= 1000000 and ada < 10000/(target10_price*1.02):
                    upbit.buy_market_order("KRW-ADA", 1000000)
                if 5000 < krw < 1000000 and ada < 10000/(target10_price*1.02):
                    upbit.buy_market_order("KRW-ADA", krw*0.9995)

            if ada > 1000000*1.001*1.2/current_price:
                upbit.sell_market_order("KRW-ADA", ada*0.9995)  
        elif middle1_time < now < middle2_time:
            ada = get_balance("ADA")
            current_price = get_current_price("KRW-ADA")
            if ada > 1000000*1.001*1.1/current_price:
                upbit.sell_market_order("KRW-ADA", ada*0.9995)  
        elif middle2_time < now < middle3_time:
            ada = get_balance("ADA")
            current_price = get_current_price("KRW-ADA")
            if ada > 1000000*1.001*1.05/current_price:
                upbit.sell_market_order("KRW-ADA", ada*0.9995)  
        elif middle3_time < now < end_time - datetime.timedelta(hours=1):
            ada = get_balance("ADA")
            current_price = get_current_price("KRW-ADA")
            if ada > 1000000*1.001*1.03/current_price or current_price > predicted_close_price:
                upbit.sell_market_order("KRW-ADA", ada*0.9995)  
        else:
            ada = get_balance("ADA")
            current_price = get_current_price("KRW-ADA")
            if ada > 1000000*1.001/current_price:
                upbit.sell_market_order("KRW-ADA", ada*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
