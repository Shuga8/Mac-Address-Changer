#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",help="interface name to change it's mac address")

parser.add_option("-m", "--mac", dest="new_mac_address",help="new MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface

new_mac_address = options.new_mac_address

print("[+] Changing mac address for " + interface + " to " + new_mac_address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
subprocess.call(["ifconfig", interface, "up"])