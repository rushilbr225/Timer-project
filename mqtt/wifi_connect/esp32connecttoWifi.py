import network
def connectToInternet():
    wifi_ssid = "Connectionfailed"
    wifi_password = "12345555"
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(wifi_ssid, wifi_password)
    if not wlan.isconnected():
        print('Connecting to network...')
        while not wlan.isconnected():
            pass

    print('Connection successful')
    print('Network config:', wlan.ifconfig())

connectToInternet()    
