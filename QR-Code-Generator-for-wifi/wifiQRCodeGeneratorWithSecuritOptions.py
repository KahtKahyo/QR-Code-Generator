import segno
from segno import helpers
from getpass import getpass

ssid = input("Enter your SSID: ")
password = getpass("Enter your password: ")
security = input("Security Options(WPA/WPA-2/WPA2-PSK): ")

wifi_settings = {
    "ssid": ssid,
    "password": password,
    "security": security,
}

wifi = segno.helpers.make_wifi(**wifi_settings)
wifi.save("Wifi-Picture.png", scale=15)
