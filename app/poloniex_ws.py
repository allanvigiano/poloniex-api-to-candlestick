import websocket
import threading
import time
import json
from threading import Thread
from datetime import datetime
from app.models import Candle

def start_thread():

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api2.poloniex.com/",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()

def on_message(ws, message):
        # print(json.loads(message)[2][0])
        #trade = json.loads(message)[2]
        is_usdt_btc = json.loads(message)[2][0] == 121
        if is_usdt_btc:
            #newCandle = Candle(=)
            print('new trade!')

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print("ON OPEN")
    def run(*args):
        ws.send(json.dumps({'command':'subscribe','channel':1002}))
        while True:
            time.sleep(1)
        ws.close()
        print("thread terminating...")
    threading.Thread(target=run).start()

def create_or_update_candle(price, timestamp, pair):
    year = int(timestamp.strftime("%Y"))
    month = int(timestamp.strftime("%m"))
    day = int(timestamp.strftime("%d"))
    hour = int(timestamp.strftime("%H"))
    minute = int(timestamp.strftime("%M"))
   
    datetime_1m = datetime.datetime(year, month, day, hour, minute)
    datetime_5m = datetime.datetime(year, month, day, hour, minute - minute % 5)
    datetime_10m = datetime.datetime(year, month, day, hour, minute - minute % 10)

    newCandle = Candle.objects.update_or_create()