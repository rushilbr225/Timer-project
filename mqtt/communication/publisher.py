from mqttconnect import mqtt_connect
import time
import ujson
import esp32led
from esp32led import onOrOff
from esp32led import led
import os

thing_name = "helloThing"
client_id = "helloThing"
topic_pub = "$aws/things/" + thing_name + "/shadow/update"
info = os.uname()

def mqtt_publish(client, topic=topic_pub, message=''):
    print("Publishing message...")
    client.publish(topic, message)
    print(message)


try:
    mqtt = mqtt_connect()
except:
    print("Unable to connect to MQTT.")
    
def connect():
    while True:
    #Check for messages.
        mesg = ujson.dumps({
            "state":{
                "reported": {
                    "device": {
                        "client": client_id,
                        "uptime": time.ticks_ms(),
                        "hardware": info[0],
                        "firmware": info[2]
                    },
                    "led": {
                        "onboard": led.value()
                    }
                }
            }
        })

    #Using the message above, the device shadow is updated.
        try:
            mqtt_publish(client=mqtt, message=mesg)
        except:
            print("Unable to publish message.")

    #Wait for 10 seconds before checking for messages and publishing a new update.
        print("Sleep for 10 seconds")
        time.sleep(10)
connect()    
