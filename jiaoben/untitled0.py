#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 10:48:09 2020

@author: yangan
"""


import threading
import time

def timer_int():
    print("every 5 secs")
    timer = threading.Timer(5, timer_int)
    timer.start()
    
timer = threading.Timer(5, timer_int)

timer.start()

while(1):
    print("every 1 sec")
    time.sleep(1)