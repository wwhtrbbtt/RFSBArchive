TOKEN = "xxx.xxx.xxx"

import websocket
from time import sleep
from threading import Thread
from json import loads
from html import unescape



def ping_thread(ws):
    """
    A thread to ping the server every 25 secs to keep the connection alive
    """
    print("Started pinging")
    while True:
        ws.send("2")
        sleep(25)

def handle_log(text):
    data = loads(text[10:])[1]
    print(f"{len(data)} new messages!")

    msgs = []

    for x in data[1:]:
        msg = unescape(x['msg'])
        msg = msg.replace('\n', '').replace('<br>', '')
        msgs.append(
            f"[{x['created']}] {x['nick']}: {msg}"
        )    

    with open("messages.html", "a") as f:
        f.write("<br>\n".join(msgs))
    return data[-1]["_id"]


def request_message(id, ws):
    """
    request a new packet with messages
    """
    packet = "42/member,[\"logmsgnext\",{\"id\":\"" + id + "\",\"mpp\":\"100\"}]"
    # print(packet)
    ws.send(packet)
    print("Sending request...")


def on_message(ws, message):
    if message.startswith("42/member,[\"logmsgnext") or message.startswith("42/member,[\"logfpgms"):
        # print("NEW CHATS!")
        ID = handle_log(message)
        # sleep(0.05)
        request_message(ID, ws)
        # print(message)

    # print(message[:20])
    
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    sleep(0.2)
    ws.send("40/member")
    sleep(0.2)
    ws.send("42/member,0[\"add user\"]")

    print("==CONNECTED==")
    Thread(target=ping_thread, args=[ws]).start()
    # Thread(target=scrape_thread, args=[ws]).start()
    sleep(2)
    ws.send("42/member,[\"logfpgmsg\",{\"mpp\":\"100\"}]")


ws = websocket.WebSocketApp("wss://zoom.raidforums.com/socket.io/?token=" + TOKEN + "&EIO=3&transport=websocket",
                            on_open = on_open,
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)

ws.run_forever()