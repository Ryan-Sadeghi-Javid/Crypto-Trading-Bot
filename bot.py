import websocket
import json
import pprint

closes = []

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"



def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")

def on_message(ws, message):
    json_message = json.loads(message)
    print(type(json_message))
    pprint.pprint(json_message)

    candle = json_message['k']

    candle_closed = candle['x']
    close = candle['c']




    if candle_closed:
        print("Candle closed at " + close)
        closes.append(float(close))
        print("closes")
        print(closes)




ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
