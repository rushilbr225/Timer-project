from mqttconnect import mqtt_connect
import time
import ujson
import esp32led
from esp32led import onOrOff

thing_name = "workshopThing"
topic_sub = "$aws/things/" + thing_name + "/shadow/update/delta"

def mqtt_subscribe(topic, msg):
    print("Message received...")
    message = ujson.loads(msg)
    if message['state']['led']:
        print(message['state']['led'])
    else:
        print(message['state']['led'])
        
    onOrOff(message['state']['led'])            
        
    print("Done")
try:
    mqtt = mqtt_connect()
    mqtt.set_callback(mqtt_subscribe)
    mqtt.subscribe(topic_sub)
    print('connected succesfully')
except:
    print("Unable to connect to MQTT.")
    
def subscribe():
    while True:
    #Check for messages.
        try:            
            mqtt.check_msg()
        except:
            print("Unable to check for messages.")
        print("Sleep for 10 seconds")
        time.sleep(10)    

subscribe()

