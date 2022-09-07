#!/usr/bin/python3
#coding=utf-8

import os
import sys
import time

def jalan(xx):
	for z in xx + "\n":
		sys.stdout.write(z)
		sys.stdout.flush()
		time.sleep(0.05)
	
os.system("clear");print("\n\n\n")
jalan(f"!. Tools ini sedang update,\n!. Coba kembali besok terimakasih")