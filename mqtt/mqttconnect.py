import esp32connecttoWifi
from simple import MQTTClient

aws_endpoint = b'ayl5o4xkfpwqy-ats.iot.ap-south-1.amazonaws.com'

#If you followed the blog, these names are already set.
thing_name = "testThing"
client_id = "testThing"
private_key = "test-private.pem.key"
private_cert = "test-certificate.pem.crt"


with open(private_key, 'r') as f:
    key = f.read()
with open(private_cert, 'r') as f:
    cert = f.read()

ssl_params = {"key":key, "cert":cert, "server_side":False}

def mqtt_connect(client=client_id, endpoint=aws_endpoint, sslp=ssl_params):
    mqtt = MQTTClient(client_id=client, server=endpoint, port=8883, keepalive=1200, ssl=True, ssl_params=sslp)
    print("Connecting to AWS IoT...")
    mqtt.connect()
    print("Done")
    return mqtt    

