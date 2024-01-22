#!/usr/bin/env python

import subprocess

interface = "eth0"

new_mac_address = "16:18:19:20:21:22"

print("[+] Changing mac address for " + interface + " to " + new_mac_address)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac_address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
