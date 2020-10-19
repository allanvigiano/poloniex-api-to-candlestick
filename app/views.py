from django.shortcuts import render
import websocket
import threading
import time
import json
from threading import Thread

def index(request):
    


    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api2.poloniex.com/",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()
    return render(request, "index.html")


def on_message(ws, message):
        # print(json.loads(message)[2][0])
        if json.loads(message)[2][0] == 121:
            print(message)

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