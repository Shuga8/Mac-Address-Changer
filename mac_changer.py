#!/usr/bin/env python

import subprocess

interface = input("Interface name >> ")

new_mac_address = input("New MAC address >> ")

print("[+] Changing mac address for " + interface + " to " + new_mac_address)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac_address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
