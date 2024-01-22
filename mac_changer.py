#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 22:33:75:28:99:12", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
