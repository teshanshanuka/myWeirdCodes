from socket import *
import wmi

ip = "192.168.0.100"
username = "Administrator"
password = "Dell@123"

try:
    print("Establishing connection to: " + ip)
    connection = wmi.WMI(ip, user=username, password=password)
    print("Connection established")
except wmi.x_wmi:
    print("Your Username and Password of "+getfqdn(ip)+" are wrong.")

input()
