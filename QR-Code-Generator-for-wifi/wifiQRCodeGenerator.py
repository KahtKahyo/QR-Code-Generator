import segno
from segno import helpers
from getpass import getpass
import json

ssid = input("Input your SSID here: ")
pswd = getpass("Enter your password: ")

wifi_settings = {
    "ssid": ssid,
    "password": pswd,
    "security": "WPA",
}

wifi = segno.helpers.make_wifi(**wifi_settings)
wifi.save("Wifi.png", scale=12)
